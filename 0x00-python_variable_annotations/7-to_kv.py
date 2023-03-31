#!/usr/bin/env python3
""" Returns a tuple from string(k) and int or float(v) """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function def"""
    return (k, (v**2))
