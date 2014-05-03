#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-02-26
@author: Ting Wang
'''

#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        previous = 0
        current = 1
        if n < 0:
            return
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            for i in range(1,n+1):
                tmp = current
                current = current + previous
                previous = tmp
            return current

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(35)
