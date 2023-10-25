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