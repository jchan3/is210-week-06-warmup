#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_04."""


def process_data(data):
    """This function determines the total sum and the average of the data in
        a tuple.

    Args:
        data(list or tuple): A list or tuple of numbers.

    Returns:
        tuple: The total sum of the data and the average of the data with
        floating point precision.

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)

    """
    count = 0
    total = 0
    for list_item in data:
        count += 1
        total = total + list_item

    avg = total/count
    return (total, float(avg))
