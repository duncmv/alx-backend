#!/usr/bin/env python3
"""Defines a MRU Cache class"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds item to cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                MRU_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", MRU_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get item by key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
