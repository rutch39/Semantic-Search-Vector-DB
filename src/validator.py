import re
from typing import Dict, Iterable, List

SLUG_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def missing_keys(payload: Dict, required: Iterable[str]) -> List[str]:
    return [k for k in required if k not in payload or payload[k] in (None, '')]


def is_valid_slug(value: str) -> bool:
    return bool(SLUG_RE.match(str(value or '').strip()))
