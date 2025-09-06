import random

RETRYABLE_CODES = {408, 425, 429, 500, 502, 503, 504}


def compute_backoff(attempt: int, base: float = 0.5, cap: float = 30.0) -> float:
    exp = min(cap, base * (2 ** max(0, attempt - 1)))
    return round(random.uniform(exp * 0.5, exp), 3)


def is_retryable_status(status_code: int) -> bool:
    return status_code in RETRYABLE_CODES
