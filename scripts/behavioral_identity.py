"""Execution identity shared by the optional runner and report comparator."""
import json


def execution_identity(record, require_generation=True):
    values = []
    for field in ('adapter', 'model'):
        value = record.get(field)
        if not isinstance(value, dict) or any(
                not isinstance(value.get(key), str) or not value[key].strip()
                for key in ('id', 'version')):
            raise ValueError(f'{field} id/version is missing')
        values.extend((value['id'], value['version']))
    mode = record.get('execution_mode')
    if mode not in {'host', 'response-only'}:
        raise ValueError('execution mode is missing')
    generation = record.get('generation')
    if generation is None and require_generation:
        raise ValueError('generation settings are unknown; establish a recorded baseline')
    if generation is not None and not isinstance(generation, dict):
        raise ValueError('generation settings must be an object')
    values.extend((mode, json.dumps(generation, sort_keys=True, allow_nan=False)))
    return tuple(values)
