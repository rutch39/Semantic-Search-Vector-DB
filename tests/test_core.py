from src.retry import compute_backoff, is_retryable_status
from src.validator import is_valid_slug, missing_keys


def test_backoff_bounds():
    delay = compute_backoff(attempt=4, base=0.5, cap=5.0)
    assert 0.0 < delay <= 5.0


def test_retryable_codes():
    assert is_retryable_status(429) is True
    assert is_retryable_status(404) is False


def test_validator_slug():
    assert is_valid_slug('api-gateway-v2') is True
    assert is_valid_slug('Invalid Slug!') is False
    assert missing_keys({'a': 1}, ['a', 'b']) == ['b']
