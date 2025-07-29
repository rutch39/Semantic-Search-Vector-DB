# Architecture Notes

## Modules
- `src/config.py`: Environment parsing and runtime defaults.
- `src/cache.py`: Bounded in-memory TTL store.
- `src/retry.py`: Jittered exponential backoff policies.
- `src/validator.py`: Input validation and slug sanitization.
- `src/metrics.py`: Lightweight counters and latency histograms.
