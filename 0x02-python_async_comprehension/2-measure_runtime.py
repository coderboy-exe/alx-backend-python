#!/usr/bin/env python3
"""A coroutine that takes no arguments"""

import asyncio
import random
import time
from functools import partial

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Executes async_comprehension 4 times and measures total time"""
    # https://docs.python.org/3.8/library/functools.html#functools.partial
    func = partial(async_comprehension)
    s = time.perf_counter()

    await asyncio.gather(func(), func(), func(), func())

    elapsed = time.perf_counter() - s

    return elapsed
