#!/usr/bin/env python3

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    def __init__(self):
        """Initializes the cache with an empty OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()