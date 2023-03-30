#!/usr/bin/env python3
""" Returns the length of a list """

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function def"""
    return [(i, len(i)) for i in lst]
