#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-17
@author: Ting Wang
'''

#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#You may not alter the values in the nodes, only nodes itself may be changed.
#Only constant memory is allowed.
#For example,
#Given this linked list: 1->2->3->4->5
#For k = 2, you should return: 2->1->4->3->5
#For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None or head.next == None or k < 2:
            return head
        next_group = head
        for i in range(k):
            if next_group != None:
                next_group = next_group.next
            else:
                return head
        new_next_group = self.reverseKGroup(next_group, k)
        prev = None
        cur = head
        while cur != next_group:
            probe = cur.next
            cur.next = prev
            prev = cur
            cur = cur.next
        if cur == prev:
            return prev
        else:
            return new_next_group