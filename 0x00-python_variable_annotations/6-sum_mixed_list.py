#!/usr/bin/env python3
""" Sums all arguments in a list of integers and floats """

from typing import Tuple


def sum_mixed_list(mxd_lst: Tuple[float, int]) -> float:
    """function def"""
    return float(sum(mxd_lst))
