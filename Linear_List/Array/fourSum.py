#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-1-2
@author: Ting Wang
'''

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# A solution set is: (-1,  0, 0, 1), (-2, -1, 1, 2), (-2,  0, 0, 2)

def fourSum(array, target):
    array.sort()
    n = len(array)
    result = []
    for i in range(n-4):
        for j in range(i+1, n-3):
            temp_pair = array[i] + array[j]
            left = j + 1
            right = n - 1
            while left < right:
                current = array[left] + array[right]
                if current == target - temp_pair:
                    temp = [array[i], array[j], array[left], array[right]]
                    if temp not in result:
                        result.append(sorted(temp))
                if current < target - temp_pair:
                    left += 1
                else:
                    right -= 1
    return result

if __name__ == '__main__':
    array = [1, 0, -1, 0, -2, 2]
    target = 0
    print fourSum(array, target)