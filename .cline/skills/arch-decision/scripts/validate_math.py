#!/usr/bin/env python3
"""Validate DAR markdown documents — check weighted scores, row totals, and sensitivity math."""

import argparse
import json
import re
import sys
from pathlib import Path

PASS = 0
FAIL = 1


def extract_json_block(text: str):
    match = re.search(r"```json\s*\n(.*?)```", text, re.DOTALL)
    if not match:
        return None
    return json.loads(match.group(1))


def validate_weights_sum(data: dict) -> list[str]:
    errors = []
    criteria = data.get("scored_criteria", [])
    total = sum(c.get("weight", 0) for c in criteria)
    if total != 100:
        errors.append(f"Weight sum is {total}, expected 100")
    return errors


def validate_weighted_scores(data: dict) -> list[str]:
    errors = []
    criteria = {c["id"]: c["weight"] for c in data.get("scored_criteria", [])}
    scores = data.get("scores", {})

    for alt_id, alt_scores in scores.items():
        for crit_id, entry in alt_scores.items():
            if crit_id not in criteria:
                continue
            weight = criteria[crit_id]
            raw = entry.get("raw", 0)
            expected_weighted = round((weight / 100) * raw, 2)
            actual_weighted = entry.get("weighted", 0)

            if actual_weighted != expected_weighted:
                errors.append(
                    f"{alt_id}.{crit_id}: weighted={actual_weighted}, "
                    f"expected={expected_weighted} "
                    f"(weight={weight}, raw={raw})"
                )
    return errors


def validate_total_scores(data: dict) -> list[str]:
    errors = []
    criteria = {c["id"]: c["weight"] for c in data.get("scored_criteria", [])}
    scores = data.get("scores", {})
    total_scores = data.get("total_scores", {})

    for alt_id, alt_scores in scores.items():
        computed = 0.0
        for crit_id, entry in alt_scores.items():
            if crit_id in criteria:
                computed += entry.get("weighted", 0)
        computed = round(computed, 2)

        declared = total_scores.get(alt_id)
        if declared is None:
            errors.append(f"{alt_id}: missing from total_scores")
            continue

        declared = round(declared, 2)
        if computed != declared:
            errors.append(f"{alt_id}: total_scores={declared}, computed={computed}")
    return errors


def expected_ranking(total_scores: dict) -> list[str]:
    return sorted(total_scores.keys(), key=lambda k: total_scores[k], reverse=True)


def validate_ranking(data: dict) -> list[str]:
    errors = []
    total_scores = data.get("total_scores", {})
    ranking = data.get("ranking", [])

    if not ranking or not total_scores:
        return errors

    expected = expected_ranking(total_scores)

    if ranking != expected:
        errors.append(f"Ranking mismatch: declared={ranking}, expected={expected}")
    return errors


def validate_raw_score_range(data: dict) -> list[str]:
    errors = []
    scores = data.get("scores", {})

    for alt_id, alt_scores in scores.items():
        for crit_id, entry in alt_scores.items():
            raw = entry.get("raw", 0)
            if raw < 0 or raw > 5:
                errors.append(f"{alt_id}.{crit_id}: raw={raw} out of range [0, 5]")
    return errors


def compute_totals_with_weights(data: dict, weights: dict[str, int]) -> dict[str, float]:
    totals = {}
    for alt_id, alt_scores in data.get("scores", {}).items():
        total = 0.0
        for crit_id, entry in alt_scores.items():
            if crit_id in weights:
                total += (weights[crit_id] / 100) * entry.get("raw", 0)
        totals[alt_id] = round(total, 2)
    return totals


def validate_sensitivity(data: dict) -> list[str]:
    errors = []
    sensitivity = data.get("sensitivity", {})
    if not sensitivity:
        return errors

    ranking = data.get("ranking", [])
    total_scores = data.get("total_scores", {})
    if len(ranking) >= 2:
        top = ranking[0]
        second = ranking[1]
        gap = round(total_scores.get(top, 0) - total_scores.get(second, 0), 2)
        declared_gap = sensitivity.get("gap_top2")
        if declared_gap is not None and round(declared_gap, 2) != gap:
            errors.append(f"Sensitivity gap_top2={declared_gap}, computed={gap}")

    scenarios = sensitivity.get("scenarios", [])
    if not scenarios:
        return errors

    criteria = data.get("scored_criteria", [])
    baseline_weights = {c["id"]: c["weight"] for c in criteria}
    baseline_ranking = data.get("ranking", [])
    weight_order = sorted(
        enumerate(criteria), key=lambda item: (-item[1].get("weight", 0), item[0])
    )
    required_pairs = {}
    if len(weight_order) >= 2:
        w1 = weight_order[0][1]["id"]
        w2 = weight_order[1][1]["id"]
        required_pairs = {"A": (w1, w2), "B": (w2, w1)}

    for scenario in scenarios:
        scenario_id = scenario.get("id", "<missing id>")
        adjusted_weights = dict(baseline_weights)
        adjusted_weights.update(scenario.get("adjusted_weights", {}))

        if sum(adjusted_weights.values()) != 100:
            errors.append(
                f"Sensitivity scenario {scenario_id}: adjusted weights sum "
                f"{sum(adjusted_weights.values())}, expected 100"
            )

        if any(weight < 0 for weight in adjusted_weights.values()):
            errors.append(f"Sensitivity scenario {scenario_id}: adjusted weights include negative values")

        source = scenario.get("source_criterion")
        target = scenario.get("target_criterion")
        shift = scenario.get("shift", 10)
        if scenario_id in required_pairs and (source, target) != required_pairs[scenario_id]:
            expected_source, expected_target = required_pairs[scenario_id]
            errors.append(
                f"Sensitivity scenario {scenario_id}: source/target=({source}, {target}), "
                f"expected=({expected_source}, {expected_target})"
            )
        if source in baseline_weights and target in baseline_weights:
            expected_source = baseline_weights[source] - shift
            expected_target = baseline_weights[target] + shift
            if adjusted_weights.get(source) != expected_source:
                errors.append(
                    f"Sensitivity scenario {scenario_id}: {source} weight="
                    f"{adjusted_weights.get(source)}, expected {expected_source}"
                )
            if adjusted_weights.get(target) != expected_target:
                errors.append(
                    f"Sensitivity scenario {scenario_id}: {target} weight="
                    f"{adjusted_weights.get(target)}, expected {expected_target}"
                )

        computed_totals = compute_totals_with_weights(data, adjusted_weights)
        declared_totals = scenario.get("total_scores", {})
        for alt_id, computed in computed_totals.items():
            declared = declared_totals.get(alt_id)
            if declared is None:
                errors.append(f"Sensitivity scenario {scenario_id}: missing total for {alt_id}")
                continue
            if round(declared, 2) != computed:
                errors.append(
                    f"Sensitivity scenario {scenario_id}: {alt_id} total={declared}, computed={computed}"
                )

        computed_ranking = expected_ranking(computed_totals)
        declared_ranking = scenario.get("ranking", [])
        if declared_ranking and declared_ranking != computed_ranking:
            errors.append(
                f"Sensitivity scenario {scenario_id}: ranking={declared_ranking}, expected={computed_ranking}"
            )

        if "ranking_change" in scenario:
            computed_change = computed_ranking != baseline_ranking
            if scenario["ranking_change"] != computed_change:
                errors.append(
                    f"Sensitivity scenario {scenario_id}: ranking_change={scenario['ranking_change']}, "
                    f"computed={computed_change}"
                )

    return errors


def validate_file(filepath: Path) -> tuple[list[str], list[str]]:
    text = filepath.read_text(encoding="utf-8")
    data = extract_json_block(text)

    if data is None:
        return [], [f"{filepath}: no JSON block found — skipping structured validation"]

    all_errors = []
    all_warnings = []

    all_errors.extend(validate_weights_sum(data))
    all_errors.extend(validate_weighted_scores(data))
    all_errors.extend(validate_total_scores(data))
    all_errors.extend(validate_ranking(data))
    all_errors.extend(validate_raw_score_range(data))
    all_errors.extend(validate_sensitivity(data))

    return all_warnings, all_errors


def main():
    parser = argparse.ArgumentParser(description="Validate DAR markdown files")
    parser.add_argument(
        "files",
        nargs="+",
        type=Path,
        help="DAR markdown files to validate",
    )
    args = parser.parse_args()

    total_errors = 0
    total_warnings = 0

    for filepath in args.files:
        if not filepath.exists():
            print(f"ERROR: {filepath} not found")
            total_errors += 1
            continue

        warnings, errors = validate_file(filepath)

        for w in warnings:
            print(f"WARN  {filepath}: {w}")
            total_warnings += 1

        for e in errors:
            print(f"ERROR {filepath}: {e}")
            total_errors += 1

        if not errors and not warnings:
            print(f"OK    {filepath}")

    print(f"\n{'=' * 60}")
    print(f"Files checked: {len(args.files)}")
    print(f"Warnings: {total_warnings}")
    print(f"Errors:   {total_errors}")

    sys.exit(FAIL if total_errors > 0 else PASS)


if __name__ == "__main__":
    main()
