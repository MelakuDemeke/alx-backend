#!/usr/bin/env python3
'''
This module defines the BasicCache class for basic caching using a dictionary
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class representing a basic cache.'''
    def put(self, key, item):
        '''Store an item in the cache if both key and item are not None.'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Retrieve item from the cache by key or return None if not found'''
        return self.cache_data.get(key, None)
