#!/usr/bin/env python3
"""Validate complete DAR matrices and sensitivity arithmetic, not decision evidence.

Weights/shifts use percentage points. Compute totals from unrounded Decimal
products, then display two decimals with ROUND_HALF_UP. Rank by unrounded totals;
exact ties may be listed in either order. Formal mode requires sensitivity cases.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import json
from pathlib import Path
import re


def number(value, label):
    if type(value) not in (int, float, Decimal):
        raise ValueError(f'{label}: expected a number, not {type(value).__name__}')
    result = Decimal(str(value))
    if not result.is_finite():
        raise ValueError(f'{label}: finite number required')
    return result


def displayed(value):
    return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def exact_totals(scores, weights):
    return {alt: sum((weights[c] * number(row[c]['raw'], f'{alt}.{c}.raw') / 100
                      for c in weights), Decimal(0)) for alt, row in scores.items()}


def check_totals(declared, totals, label, errors):
    if not isinstance(declared, dict) or set(declared) != set(totals):
        errors.append(f'{label}: totals must contain exactly the scored alternatives')
        return
    for alt, expected in totals.items():
        if number(declared[alt], f'{label}.{alt}') != displayed(expected):
            errors.append(f'{label}.{alt}: expected {displayed(expected)} from unrounded products')


def check_ranking(ranking, totals, label, errors):
    if not isinstance(ranking, list) or any(not isinstance(x, str) for x in ranking):
        errors.append(f'{label}: ranking must be an array of alternative IDs')
        return
    if len(ranking) != len(totals) or set(ranking) != set(totals):
        errors.append(f'{label}: ranking must include every alternative exactly once')
    elif any(totals[a] < totals[b] for a, b in zip(ranking, ranking[1:])):
        errors.append(f'{label}: ranking contradicts unrounded totals')


def ordering(totals):
    names = sorted(totals)
    return {(a, b): (totals[a] > totals[b]) - (totals[a] < totals[b])
            for i, a in enumerate(names) for b in names[i + 1:]}


def validate_data(data):
    errors = []
    try:
        if not isinstance(data, dict):
            raise ValueError('DAR summary must be an object')
        criteria, scores = data.get('scored_criteria'), data.get('scores')
        if not isinstance(criteria, list) or not criteria:
            raise ValueError('scored_criteria must be a nonempty array')
        weights = {}
        for item in criteria:
            if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id'].strip():
                raise ValueError('each criterion needs a nonempty string ID')
            cid = item['id']
            if cid in weights:
                raise ValueError(f'duplicate criterion {cid}')
            weights[cid] = number(item.get('weight'), f'{cid}.weight')
            if not 0 <= weights[cid] <= 100:
                raise ValueError(f'{cid}.weight: must be in [0, 100]')
        if sum(weights.values()) != 100:
            errors.append('criterion weights must sum to exactly 100')
        if not isinstance(scores, dict) or not scores:
            raise ValueError('scores must contain at least one eligible alternative')
        for alt, row in scores.items():
            if not isinstance(alt, str) or not alt.strip():
                raise ValueError('alternative IDs must be nonempty strings')
            if not isinstance(row, dict) or set(row) != set(weights):
                raise ValueError(f'{alt}: score every criterion exactly once; unknown criteria are invalid')
            for cid, entry in row.items():
                if not isinstance(entry, dict):
                    raise ValueError(f'{alt}.{cid}: score must be an object')
                raw = number(entry.get('raw'), f'{alt}.{cid}.raw')
                if not 0 <= raw <= 5:
                    raise ValueError(f'{alt}.{cid}.raw: must be in [0, 5]')
                actual = number(entry.get('weighted'), f'{alt}.{cid}.weighted')
                expected = displayed(weights[cid] * raw / 100)
                if actual != expected:
                    errors.append(f'{alt}.{cid}: weighted={actual}, expected={expected}')
        totals = exact_totals(scores, weights)
        check_totals(data.get('total_scores'), totals, 'baseline', errors)
        check_ranking(data.get('ranking'), totals, 'baseline', errors)
        sensitivity = data.get('sensitivity', {})
        if not isinstance(sensitivity, dict):
            raise ValueError('sensitivity must be an object')
        if 'gap_top2' in sensitivity:
            if len(totals) < 2:
                raise ValueError('gap_top2 requires two alternatives')
            ordered = sorted(totals.values(), reverse=True)
            if number(sensitivity['gap_top2'], 'gap_top2') != displayed(ordered[0] - ordered[1]):
                errors.append('gap_top2 does not match unrounded baseline totals')
        scenarios = sensitivity.get('scenarios', [])
        if not isinstance(scenarios, list):
            raise ValueError('sensitivity.scenarios must be an array')
        if data.get('mode', '').lower() == 'formal' and len(weights) > 1 and len(scores) > 1 and not scenarios:
            errors.append('formal comparison requires sensitivity scenarios')
        seen = set()
        for scenario in scenarios:
            if not isinstance(scenario, dict) or not isinstance(scenario.get('id'), str) or not scenario['id'].strip():
                raise ValueError('sensitivity scenario requires an ID')
            sid = scenario['id']
            if sid in seen:
                raise ValueError(f'duplicate sensitivity scenario {sid}')
            seen.add(sid)
            changes = scenario.get('adjusted_weights')
            if not isinstance(changes, dict) or not changes or not set(changes) <= set(weights):
                raise ValueError(f'{sid}: adjusted_weights must name known criteria')
            adjusted = dict(weights)
            adjusted.update({c: number(v, f'{sid}.{c}') for c, v in changes.items()})
            if sum(adjusted.values()) != 100 or any(not 0 <= v <= 100 for v in adjusted.values()):
                raise ValueError(f'{sid}: adjusted weights must be in [0, 100] and sum to 100')
            transfer = {'source_criterion', 'target_criterion', 'shift'}
            if transfer & scenario.keys():
                if not transfer <= scenario.keys():
                    raise ValueError(f'{sid}: transfer requires source, target and shift')
                source, target = scenario['source_criterion'], scenario['target_criterion']
                if not isinstance(source, str) or not isinstance(target, str) or source not in weights or target not in weights or source == target:
                    raise ValueError(f'{sid}: distinct known source/target criteria required')
                shift = number(scenario['shift'], f'{sid}.shift')
                if not 0 < shift <= weights[source] or weights[target] + shift > 100:
                    raise ValueError(f'{sid}: transfer exceeds available percentage points')
                expected = dict(weights)
                expected[source] -= shift
                expected[target] += shift
                if adjusted != expected:
                    errors.append(f'{sid}: adjusted weights differ from the declared transfer')
            alternative_totals = exact_totals(scores, adjusted)
            check_totals(scenario.get('total_scores'), alternative_totals, sid, errors)
            check_ranking(scenario.get('ranking'), alternative_totals, sid, errors)
            if type(scenario.get('ranking_change')) is not bool:
                errors.append(f'{sid}: ranking_change must be boolean')
            elif scenario['ranking_change'] != (ordering(totals) != ordering(alternative_totals)):
                errors.append(f'{sid}: ranking_change does not match computed ordering/ties')
    except (ValueError, InvalidOperation, AttributeError) as exc:
        errors.append(str(exc))
    return errors


def extract_json_block(text):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'duplicate JSON key: {key}')
            result[key] = value
        return result

    summaries = []
    for match in re.finditer(r'^```json\s*\n(.*?)^```\s*$', text, re.M | re.S):
        value = json.loads(match[1], parse_float=Decimal, object_pairs_hook=unique_object,
                           parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f'invalid JSON constant {x}')))
        if isinstance(value, dict) and 'scored_criteria' in value:
            summaries.append(value)
    if len(summaries) != 1:
        raise ValueError('expected exactly one JSON DAR summary containing scored_criteria')
    return summaries[0]


def validate_file(filepath):
    try:
        return [], validate_data(extract_json_block(Path(filepath).read_text(encoding='utf-8')))
    except (OSError, ValueError) as exc:
        return [], [str(exc)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    count = 0
    for filepath in args.files:
        _, errors = validate_file(filepath)
        for error in errors:
            print(f'ERROR {filepath}: {error}')
        if not errors:
            print(f'OK {filepath}')
        count += len(errors)
    print(f'Files checked: {len(args.files)}; errors: {count}')
    return int(bool(count))


if __name__ == '__main__':
    raise SystemExit(main())
