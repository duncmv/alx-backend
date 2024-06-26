#!/usr/bin/env python3
"""defines a lifo Cache"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            self.cache_data.pop(last_key)
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """get item by key"""
        return self.cache_data.get(key)
                