#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-02-21
@author: Ting Wang
inference: https://github.com/baiyubin/leetcode/blob/master/nextPermutation/main.py
'''

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

def nextPermutation(seq):
    size = len(seq)
    if size <= 1:
        return
    # find the Partition Number
    low =  size - 2
    high = size - 1
    while seq[low] >= seq[high]:
        if low == high - 1:
            low -= 1
            high = size - 1
            if low < 0:
                break
        else:
            high -= 1
    if low < 0:
        raise Exception("End of Permutation")
    # swap seq[low] and seq[high] if low >= 0
    seq[low], seq[high] = seq[high], seq[low]
    # reverse the low+1 to size-1
    seq[low + 1 : size] = seq[size - 1 : low : -1]
    return seq

if __name__ == '__main__':
    seq = [1, 5, 3, 4, 2]
    #print nextPermutation(seq)
    from factorial import factorial
    for i in range(factorial(len(seq))):
        try:
            print nextPermutation(seq)
        except:
            print("End of permutations")
            break
        else:
            print(seq)
