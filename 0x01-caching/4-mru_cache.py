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
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        else:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
