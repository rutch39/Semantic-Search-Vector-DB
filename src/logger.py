from datetime import datetime, timezone


def format_event(level: str, message: str, **fields) -> str:
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    extra = ' '.join(f'{k}={v}' for k, v in sorted(fields.items()))
    return f'[{ts}] {level.upper():<5} {message}' + (f' | {extra}' if extra else '')
