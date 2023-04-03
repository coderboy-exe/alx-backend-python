#!/usr/bin/env python3
"""
    Takes an integer (max_delay) and returns asyncio.Task
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function definition"""
    # https://superfastpython.com/asyncio-return-value/
    return asyncio.create_task(wait_random(max_delay))
