#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-07
@author: Ting Wang
#A LITTLE HARD
'''

#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#For example,
#Given 1->2->3->3->4->4->5, return 1->2->5.
#Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head.next
        if head.val == p.val:
            while p != None and head.val == p.val:
                tmp = p
                p = p.next
                del tmp
            del head
            return self.deleteDuplicates(p)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head

