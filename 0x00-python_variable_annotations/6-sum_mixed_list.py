#!/usr/bin/env python3
""" Sums all arguments in a list of integers and floats """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function def"""
    return float(sum(mxd_lst))
