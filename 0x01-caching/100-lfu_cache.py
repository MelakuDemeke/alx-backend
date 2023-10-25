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

    def put(self, key, item):
        """Add an item to the cache.

        If the cache is full, the least frequently used item is removed.

        Args:
            key (str): The key to store the item under.
            item: The item to cache.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq.pop()
                self.cache_data.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.keys_freq.insert(0, (key, 0))
        else:
            self.cache_data[key] = item
            self._reorder_items(key)

    def get(self, key):
        """Retrieve an item from the cache by its key.

        When getting an item, the cache is updated to reflect its usage.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The cached item or None if not found.
        """
        pass