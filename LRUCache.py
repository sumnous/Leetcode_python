#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-18
@author: Ting Wang
'''
#Design and implement a data structure for Least Recently Used (LRU) cache.
#It should support the following operations: get and set.
#get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#set(key, value) - Set or insert the value if the key is not already present.
#When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.Dict = collections.OrderedDict()
        self.capacity = capacity
        self.numItems = 0

    # @return an integer
    def get(self, key):
        if self.Dict.has_key(key):
            value = self.Dict[key]
            del self.Dict[key]
            self.Dict[key] = value
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.Dict.has_key(key):
            del self.Dict[key]
            self.Dict[key] = value
            return
        else:
            if self.numItems == self.capacity:
                self.Dict.popitem(last = False)
                self.numItems -= 1
            self.Dict[key] = value
            self.numItems += 1
            return
