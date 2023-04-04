#!/usr/bin/env python3
"""A coroutine that takes no arguments"""

import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Comprehenses over async_generator then returns the 10 random numbers"""
    result = [i async for i in async_generator()]
    return result
