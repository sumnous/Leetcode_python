#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-02-28
@author: Ting Wang
'''

#The gray code is a binary numeral system where two successive values differ in only one bit.
#Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
#A gray code sequence must begin with 0.
#For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#00 - 0
#01 - 1
#11 - 3
#10 - 2
#Note:
#For a given n, a gray code sequence is not uniquely defined.
#For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
#For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        graylist = [0] * n
        i = 0
        graycode = [[0] * n]
        while i < (pow(2, n)-1):
            for j in reversed(range(n)):
                tmp = list(graylist)
                if graylist[j] == 0:
                    graylist[j] = 1
                else:
                    graylist[j] = 0
                if graylist not in graycode:
                    break
                else:
                    graylist = tmp
            graycode.append(list(graylist))
            i += 1
        result = []
        for x in graycode:
            re = 0
            for i in range(n):
                re += x[i] * pow(2, n-i-1)
            result.append(re)
        return result

if __name__ == '__main__':
    s = Solution()
    print s.grayCode(2)