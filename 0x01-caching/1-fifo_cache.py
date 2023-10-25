#!/usr/bin/env python3
"""First-In First-Out (FIFO) caching module."""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """A caching mechanism that uses First-In First-Out (FIFO) strategy"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()