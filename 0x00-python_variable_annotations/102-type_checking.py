#!/usr/bin/env python3
""" Returns elements of an array in a specific range """

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """function definition"""
    zoomed_in: Tuple[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: Tuple[int, int, int]  = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
