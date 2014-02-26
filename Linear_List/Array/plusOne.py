#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-01-26
@author: Ting Wang
'''
#Given a non-negative number represented as an array of digits, plus one to the number.
#The digits are stored such that the most significant digit is at the head of the list.
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] + 1 == 10:
                digits[i] = 0
                if i == 0:
                    def insert_begin(digits):
                        digits.append(0)
                        for i in reversed(range(len(digits)-1)):
                            digits[i+1] = digits[i]
                        digits[0] = 1
                    insert_begin(digits)
            else:
                digits[i] += 1
                break
        print digits
        return digits

if __name__ == '__main__':
    s = Solution()
    #s.plusOne([1,2,3,4])
    #s.plusOne([1,9,9])
    #s.plusOne([9,9,9])
    s.plusOne([1])
