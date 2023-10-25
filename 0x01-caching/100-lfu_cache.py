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
