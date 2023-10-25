#!/usr/bin/env python3

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    Represents a Most Recently Used (MRU) caching mechanism.
    Inherits from BaseCaching.
    """
    def __init__(self):
        """Initializes the cache with an empty OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the MRU cache.

        :param key: The key to associate with the item.
        :param item: The item to be stored.
        """
        if key is None or item is None:
            return
