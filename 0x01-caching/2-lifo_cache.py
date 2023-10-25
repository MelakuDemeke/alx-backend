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
        """Add an item to the cache, implementing LIFO if the limit is reached
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item