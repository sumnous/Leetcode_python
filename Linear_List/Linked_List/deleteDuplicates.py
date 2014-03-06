#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-07
@author: Ting Wang
'''

#Given a sorted linked list, delete all duplicates such that each element appear only once.
#For example,
#Given 1->1->2, return 1->2.
#Given 1->1->2->3->3, return 1->2->3.
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        if head == None or head.next == None:
            return head
        p = head.next
        while p != None:
            if p.val == head.val:
                head.next = p.next
                p = p.next
            else:
                head = p
                p = p.next
        return dummy.next

