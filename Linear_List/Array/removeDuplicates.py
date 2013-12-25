#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-09
@author: Ting Wang
'''

# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example, Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].

def removeDuplicates(sorted_array):
    index = 0
    if len(sorted_array) == 0:
        return 0
    for i in range(1, len(sorted_array)):
        if sorted_array[index] != sorted_array[i]:
            index += 1
            sorted_array[index] = sorted_array[i]
    return index+1

def removeDuplicates_extra_space_1(sorted_array):
    return list(set(sorted_array))

def removeDuplicates_extra_space_2(sorted_array):
    sorted_array = dict.fromkeys(sorted_array)
    return sorted_array.keys()

def removeDuplicates_extra_space_3(sorted_array):
    result = []
    for element in sorted_array:
        if element not in result:
            result.append(element)
    return result

if __name__ == '__main__':
    A = [1,1,2,2,2,3,3]
    print A[0:removeDuplicates(A)]
    #print removeDuplicates_extra_space_1(A)
    #print removeDuplicates_extra_space_2(A)
    #print removeDuplicates_extra_space_3(A)
