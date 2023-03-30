#!/usr/bin/env python3
""" Returns function that multiplies a float ny multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return (lambda x: x * multiplier)
