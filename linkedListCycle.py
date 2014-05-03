#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-18
@author: Ting Wang
'''

#Given a linked list, determine if it has a cycle in it.
#Follow up:
#Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False