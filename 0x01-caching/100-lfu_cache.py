#!/usr/bin/env python3
"""Least Frequently Used (LFU) caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


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

    def reorder_items_based_on_mru(self, mru_key):
        """Reorder items in the cache based on the given key's usage frequency.

        Args:
            key (str): The key to reorder based on its usage frequency.
        """
        max_pos = []
        mru_fre = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_fre = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key_freq[1] < self.keys_freq[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.keys_freq[pos][1] > mru_fre:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_fre])

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
            self.reorder_items_based_on_mru(key)

    def get(self, key):
        """Retrieve an item from the cache by its key.

        When getting an item, the cache is updated to reflect its usage.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The cached item or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.reorder_items_based_on_mru(key)
        return self.cache_data.get(key, None)
