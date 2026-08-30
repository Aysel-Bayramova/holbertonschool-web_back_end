#!/usr/bin/env python3
"""
This module contains a simple helper function for pagination purposes.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indexes for a given
    pagination size and page number.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
