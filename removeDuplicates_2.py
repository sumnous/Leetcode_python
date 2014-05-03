#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-09
@author: Ting Wang
'''

# Follow up for ”Remove Duplicates”: What if duplicates are allowed at most twice?
# For example, Given sorted array A = [1,1,1,2,2,3],
# Your function should return length = 5, and A is now [1,1,2,2,3]

def removeDuplicates_2(sorted_array):
    index = 2
    if len(sorted_array) <=2 :
        return len(sorted_array)
    for i in range(2, len(sorted_array)):
        if sorted_array[i] != sorted_array[index-2]:
            print "i=",i, "index=",index
            sorted_array[index] = sorted_array[i]
            index += 1
    return index

if __name__ == '__main__':
    A = [1,1,1,2,2,2,3,3,3,3]
    print A[0:removeDuplicates_2(A)]