#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-28
@author: Ting Wang
'''

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example, Given [100, 4, 200, 1, 3, 2], the longest consecutive elements sequence is [1, 2, 3, 4].
# Return its length: 4. Your algorithm should run in O(n) complexity.

def longestConsecutive(input):
    longest = 0
    # using hashtable to record if the element is used
    dict = {}
    for x in input:
        dict[x] = False
    for x in input:
        if dict[x] == True:
            continue
        length = 1
        dict[x] = True
        right = x
        left = x
        while right+1 in dict.keys(): # increasing the element
            dict[right+1] = True
            right += 1
        while left-1 in dict.keys(): # decreasing the element
            dict[left-1] = True
            left -= 1
        length = right - left + 1
        longest = max(length, longest)
    return longest

if __name__ == '__main__':
    input = [100, 4, 200, 1, 3, 2]
    print longestConsecutive(input)