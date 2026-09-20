#!/usr/bin/env python3
"""Opt-in response-only adapter for a configured Chat Completions endpoint."""
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None  # Never forward authorization to a redirected endpoint.


def complete(request):
    if request.get('mode') == 'activation':
        return {'status': 'unavailable', 'reason': 'The response-only adapter cannot observe host skill-loading events; use a host adapter.'}
    base, model = os.getenv('ARCH_TEST_API_BASE', ''), os.getenv('ARCH_TEST_MODEL', '')
    if not base or not model:
        return {'status': 'unavailable', 'reason': 'Set ARCH_TEST_API_BASE and ARCH_TEST_MODEL; no model was invoked.'}
    parsed = urlsplit(base)
    if (parsed.username or parsed.password or parsed.query or parsed.fragment or not parsed.hostname or
            (parsed.scheme != 'https' and not (parsed.scheme == 'http' and parsed.hostname in {'localhost', '127.0.0.1', '::1'}))):
        return {'status': 'error', 'reason': 'Use HTTPS or a loopback HTTP endpoint without embedded credentials.'}
    token_limit = int(os.getenv('ARCH_TEST_MAX_TOKENS', '2048'))
    if not 1 <= token_limit <= 16384:
        return {'status': 'error', 'reason': 'ARCH_TEST_MAX_TOKENS must be 1..16384.'}
    instructions = (Path(request['skill_root']) / 'SKILL.md').read_text(encoding='utf-8')
    system = ('Apply the following skill to the user request. This is a response-only test. '
              'You have no filesystem or tool access; do not claim you used tools or read references.\n\n' + instructions)
    payload = {'model': model, 'messages': [{'role': 'system', 'content': system}] + request['messages'],
               'max_tokens': token_limit, 'stream': False}
    headers = {'Content-Type': 'application/json'}
    key = os.getenv('ARCH_TEST_API_KEY')
    if key:
        headers['Authorization'] = f'Bearer {key}'
    req = Request(base.rstrip('/') + '/chat/completions', json.dumps(payload).encode(), headers)
    try:
        with build_opener(NoRedirect).open(req, timeout=max(1, request['timeout'] - 5)) as response:
            result = json.load(response)
    except HTTPError as exc:
        return {'status': 'unavailable' if exc.code in {401, 403, 429} else 'error',
                'reason': f'Provider HTTP {exc.code}; no response body or credential retained.'}
    except (URLError, TimeoutError, OSError):
        return {'status': 'unavailable', 'reason': 'Provider unreachable; no model result available.'}
    except ValueError:
        return {'status': 'error', 'reason': 'Provider returned invalid JSON.'}
    if (not isinstance(result, dict) or not isinstance(result.get('choices'), list)
            or not result['choices'] or not isinstance(result['choices'][0], dict)):
        return {'status': 'error', 'reason': 'Provider returned an invalid choices envelope.'}
    choice = result['choices'][0]
    if choice.get('finish_reason') != 'stop':
        return {'status': 'error', 'reason': 'Provider did not return a complete text answer.'}
    message = choice.get('message')
    if not isinstance(message, dict) or not isinstance(message.get('content'), str) or not message['content'].strip():
        return {'status': 'error', 'reason': 'Provider returned no nonempty text answer.'}
    usage = result.get('usage')
    if usage is None:
        usage = {}
    if not isinstance(usage, dict):
        return {'status': 'error', 'reason': 'Provider returned invalid token usage.'}
    tokens = usage.get('total_tokens')
    if tokens is not None and (type(tokens) is not int or tokens < 0):
        return {'status': 'error', 'reason': 'Provider returned invalid token usage.'}
    return {'status': 'ok', 'response': choice['message']['content'], 'execution_mode': 'response-only',
            'adapter': {'id': 'chat-completion', 'version': '1.0.1'},
            'model': {'id': model, 'version': result.get('model') or model},
            'model_version_note': 'Provider-reported ID; an alias does not prove an immutable revision.',
            'generation': {'max_tokens': token_limit, 'stream': False},
            'total_tokens': tokens, 'capabilities_used': None}


if __name__ == '__main__':
    try:
        output = complete(json.load(sys.stdin))
    except (OSError, ValueError, KeyError, IndexError, TypeError):
        output = {'status': 'error', 'reason': 'Invalid adapter input, configuration or provider response.'}
    print(json.dumps(output))
