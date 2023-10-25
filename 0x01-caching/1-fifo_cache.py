#!/usr/bin/env python3
"""First-In First-Out (FIFO) caching module."""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """A caching mechanism that uses First-In First-Out (FIFO) strategy"""
    def __init__(self):
        """Initialize the cache using an ordered dictionary"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache, implementing FIFO if the limit is reached
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item from the cache by key"""
        return self.cache_data.get(key, None)
