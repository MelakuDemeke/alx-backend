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

    def reorder_items_based_on_mru(self, most_recently_used_key):
        """Reorder items in the cache based on the given key's usage frequency.

        Args:
            key (str): The key to reorder based on its usage frequency.
        """
        max_positions = []
        mru_frequency = 0
        mru_position = 0
        insertion_position = 0

        for i, (key, frequency) in enumerate(self.keys_freq):
            if key == most_recently_used_key:
                mru_frequency = frequency + 1
                mru_position = i
                break
            elif not max_positions or frequency < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)

        max_positions.reverse()

        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_frequency:
                break
            insertion_position = pos

        self.keys_freq.pop(mru_position)
        self.keys_freq.insert(insertion_position, [most_recently_used_key, mru_frequency])
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
