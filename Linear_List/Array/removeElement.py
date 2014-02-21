#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-01-21
@author: Ting Wang
'''

# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

def removeElement(array, value):
    count = 0
    for i in range(len(array)):
        if array[i] != value:
            array[count] = array[i]
            count += 1
    return count

if __name__ == '__main__':
    array = [1, 2, 2, 3, 4, 5, 6, 1, 2, 2, 7]
    print removeElement(array, 2)