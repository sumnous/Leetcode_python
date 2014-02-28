#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-01-28
@author: Ting Wang
'''

#You are given two linked lists representing two non-negative numbers.
#The digits are stored in reverse order and each of their nodes contain a single digit.
#Add the two numbers and return it as a linked list.
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        len1 = 0
        len2 = 0
        head = l1
        while head != None:
            len1 += 1
            head = head.next
        head = l2
        while head != None:
            len2 += 1
            head = head.next
        if len1 >= len2:
            large = l1
            small = l2
        else:
            large = l2
            small = l1
        flag = 0
        sum = None
        while small != None:
            num = small.val + large.val + flag
            flag = num / 10
            num -= flag * 10
            if sum == None:
                sum = ListNode(num)
                result = sum
            else:
                sum.next = ListNode(num)
                sum = sum.next
            small = small.next
            large = large.next
        while large != None:
            num = large.val + flag
            flag = num / 10
            num -= flag * 10
            sum.next = ListNode(num)
            sum = sum.next
            large = large.next
        if flag != 0:
            sum.next = ListNode(flag)
        return result

