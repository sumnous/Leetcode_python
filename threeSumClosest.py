#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-1-2
@author: Ting Wang
'''

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

import math

def threeSumClosest(array, target):
    array.sort()
    n = len(array)
    result = [1<<33, -1, -1, -1]
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            current = array[left] + array[right]
            distance = math.fabs(target - array[i])
            if distance < result[0]:
                result = [distance, array[i], array[left], array[right]]
            if current < distance:
                left += 1
            else:
                right -= 1
    return result[1] + result[2] + result[3]

if __name__ == '__main__':
    array = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest(array, target))