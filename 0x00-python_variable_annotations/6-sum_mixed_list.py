#!/usr/bin/env python3

from typing import List, Union

"""
Contains a function for summing a list of values
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list of integers and floats and returns the
    sum of all the numbers in the list as float"""
    return float(sum(mxd_lst))
