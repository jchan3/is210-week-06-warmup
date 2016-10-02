#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_05."""


def flip_keys(to_flip):
    """This function determines .

    Args:
        to_flip(list): A list with nested, immutable sequences inside it.

    Returns:
        list: The original list with its inner elements reversed.

    Examples:

        >>> NEW = flip_keys(LIST)
        [(3, 2, 1), 'cba']

    """
    count = 0
    for list_item in to_flip:
        to_flip[count] = list_item[::-1]
        count += 1

    return
