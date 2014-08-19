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

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        n = len(num)
        result = []
        for i in xrange(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                current = num[left] + num[right]
                if current == -num[i]:
                    triplets = [num[i], num[left], num[right]]
                    triplets.sort()
                    if triplets not in result:
                        result.append(triplets)
                if current < -num[i]:
                    left += 1
                else:
                    right -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    array = [-1, 0, 1, 2, -1, -4]
    #array = [0,0,0]
    print s.threeSum(array)