#!/usr/bin/env python3
"""defines a BasicCache class"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic Cache class"""
    def put(self, key, item):
        """add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        return self.cache_data.get(key)
