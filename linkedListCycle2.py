#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-18
@author: Ting Wang
'''

#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#Follow up:
#Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow2 != slow:
                    slow = slow.next
                    slow2 = slow2.next
                return slow2
        return None
