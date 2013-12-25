#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-11
@author: Ting Wang
'''

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

import math

def searchRotatedArray(data, target):
    first = 0
    last = len(data)
    while first != last:
        mid = int(math.floor((first + last) / 2))
        if target == data[mid]:
            return mid
        if data[first] <= data[mid]:
            if target >= data[first] and target < data[mid]:
                last = mid
            else:
                first = mid +1
        else:
            if target > data[mid] and target <= data[last - 1]:
                first = mid +1
            else:
                last = mid
    return -1

if __name__ == '__main__':
    A = [4,5,6,7,0,1,2,3]
    print searchRotatedArray(A, 3)


