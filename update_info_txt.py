#!/usr/bin/env python3
import time
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent


def update_last_updated_timestamp() -> None:
    """Update the last updated timestamp."""
    info_path = ROOT_DIR / 'info.txt'
    with open(info_path, mode='w') as file:
        file.write(f'last_update_timestamp = {int(time.time())}')


update_last_updated_timestamp()