from collections import defaultdict
from typing import Dict


class MetricsRegistry:
    def __init__(self):
        self._counters: Dict[str, int] = defaultdict(int)
        self._timings: Dict[str, list] = defaultdict(list)

    def inc(self, name: str, value: int = 1) -> None:
        self._counters[name] += value

    def observe_ms(self, name: str, elapsed_ms: float) -> None:
        self._timings[name].append(round(float(elapsed_ms), 2))

    def snapshot(self) -> Dict:
        return {'counters': dict(self._counters), 'samples': {k: len(v) for k, v in self._timings.items()}}


def moving_avg(values: list, window: int = 5) -> float:
    subset = values[-max(1, window):]
    return round(sum(subset) / len(subset), 3) if subset else 0.0
