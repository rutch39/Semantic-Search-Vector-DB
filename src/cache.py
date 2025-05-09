import time
from typing import Any, Optional


class MemoryCache:
    def __init__(self, default_ttl: int = 60, max_items: int = 512):
        self.default_ttl = default_ttl
        self.max_items = max_items
        self._store = {}

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        if len(self._store) >= self.max_items:
            self.purge_expired()
        exp = time.monotonic() + (ttl if ttl is not None else self.default_ttl)
        self._store[key] = (value, exp)

    def get(self, key: str, default: Any = None) -> Any:
        entry = self._store.get(key)
        if not entry:
            return default
        val, exp = entry
        if time.monotonic() >= exp:
            self._store.pop(key, None)
            return default
        return val

    def purge_expired(self) -> int:
        now = time.monotonic()
        stale = [k for k, (_, exp) in self._store.items() if exp <= now]
        for k in stale:
            self._store.pop(k, None)
        return len(stale)
