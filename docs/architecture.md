# Architecture Notes

## Modules
- `src/config.py`: Environment parsing and runtime defaults.
- `src/cache.py`: Bounded in-memory TTL store.
- `src/retry.py`: Jittered exponential backoff policies.
- `src/validator.py`: Input validation and slug sanitization.
- `src/metrics.py`: Lightweight counters and latency histograms.

### Configuration Precedence
Process environment variables always override default values defined in `config/defaults.json`.

### Logging Conventions
Emit UTC ISO-8601 timestamps with flat `key=value` context fields for easy log parsing.
