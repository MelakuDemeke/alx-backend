#!/usr/bin/env python3
"""Last-In First-Out (LIFO) caching module."""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """A caching mechanism that uses Last-In First-Out (LIFO) strategy."""
    def __init__(self):
        """Initialize the cache using an ordered dictionary."""
        super().__init__()
        self.cache_data = OrderedDict()
    def put(self, key, item):
        pass