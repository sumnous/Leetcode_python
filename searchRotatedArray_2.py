#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-11
@author: Ting Wang
'''

# Follow up for ”Search in Rotated Sorted Array”: What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.

import math

def searchRotatedArray_2(data, target):
    first = 0
    last = len(data)
    while first != last:
        mid = int(math.floor((first + last) / 2))
        if target == data[mid]:
            return True
        if data[first] < data[mid]:
            if target >= data[first] and target < data[mid]:
                last = mid
            else:
                first = mid +1
        elif data[first] > data[mid]:
            if target > data[mid] and target <= data[last - 1]:
                first = mid +1
            else:
                last = mid
        else:
            first += 1
    return False

if __name__ == '__main__':
    A = [1,1,2,3,1,1,1]
    print searchRotatedArray_2(A, 2)