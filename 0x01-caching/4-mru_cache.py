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
        pass
