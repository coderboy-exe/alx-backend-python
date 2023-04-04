#!/usr/bin/env python3
"""A coroutine that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yiedls a random number for every iteration of the loop"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
