#!/usr/bin/env python3
"""
    Concurrent coroutinesi | measures the total execution time of wait_n
"""

import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function definition"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s

    return elapsed / n
