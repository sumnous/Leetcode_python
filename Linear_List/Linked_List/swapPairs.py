#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-17
@author: Ting Wang
& used some time, about even or odd of array
'''

#Given a linked list, swap every two adjacent nodes and return its head.
#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.
#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        after = cur.next
        while cur != None and cur.next != None:
            if after.next == None:
                return dummy.next
            cur.next = after.next
            if after.next.next == None:
                after.next = None
            else:
                after.next = after.next.next
            cur.next.next = after
            cur = after
            after = after.next
        return dummy.next

