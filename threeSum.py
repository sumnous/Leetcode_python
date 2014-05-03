#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-1-2
@author: Ting Wang
'''

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
# For example, given array S = {-1 0 1 2 -1 -4}.
# A solution set is: (-1, 0, 1)  (-1, -1, 2)

def threeSum(array, target):
    array.sort()
    n = len(array)
    result = []
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            current = array[left] + array[right]
            if current == target - array[i]:
                temp = [array[i], array[left], array[right]]
                if temp not in result:
                    result.append(sorted(temp))
            if current < target - array[i]:
                left += 1
            else:
                right -= 1
    return result

if __name__ == '__main__':
    array = [-1, 0, 1, 2, -1, -4]
    target = 0
    print threeSum(array, target)