#!/usr/bin/env python3
"""Least Recently Used (LRU) caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """A caching mechanism that uses Least Recently Used (LRU) strategy.
    """
    def __init__(self):
        """Initialize the cache using an ordered dictionary."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache, implementing LRU if the limit is reached.
        """
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieve an item from the cache by key,
        updating its position as themost recently used.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
