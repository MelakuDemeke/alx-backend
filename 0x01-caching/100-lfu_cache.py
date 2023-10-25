#!/usr/bin/env python3
"""Least Frequently Used (LFU) caching module.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used (LFU) Cache implementation.

    This class represents a caching mechanism that stores and retrieves items
    based on the LFU
    (Least Frequently Used) algorithm.

    Attributes:
        cache_data (OrderedDict): A dictionary-like data structure to store
                                    cached items.
        keys_freq (list): A list to track key frequencies in the cache.
    """

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def _reorder_items(self, key):
        """Reorder items in the cache based on the given key's usage frequency.

        Args:
            key (str): The key to reorder based on its usage frequency.
        """
        current_freq = 0
        for i, (k, freq) in enumerate(self.keys_freq):
            if k == key:
                current_freq = freq
                self.keys_freq.pop(i)
                break

        insert_index = 0
        for i, (k, freq) in enumerate(self.keys_freq):
            if freq > current_freq:
                insert_index = i + 1
            else:
                break
        self.keys_freq.insert(insert_index, (key, current_freq + 1))
