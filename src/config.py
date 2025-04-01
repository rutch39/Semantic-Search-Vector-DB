import os
from dataclasses import dataclass


@dataclass
class RuntimeConfig:
    env: str = 'production'
    timeout_sec: int = 30
    max_retries: int = 3
    debug: bool = False


def load_config() -> RuntimeConfig:
    return RuntimeConfig(
        env=os.getenv('APP_ENV', 'production'),
        timeout_sec=int(os.getenv('TIMEOUT_SEC', '30')),
        max_retries=int(os.getenv('MAX_RETRIES', '3')),
        debug=os.getenv('DEBUG', '0').lower() in {'1', 'true', 'yes'},
    )
