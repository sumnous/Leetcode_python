#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-13
@author: Ting Wang
'''

#Given a list, rotate the list to the right by k places, where k is non-negative.
#For example:
#Given 1->2->3->4->5->NULL and k = 2,
#return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None or k == 0:
            return head
        p = head
        length = 1
        while p.next != None:
            length += 1
            p = p.next
        k = length - k % length
        p.next = head
        for i in range(k):
            p = p.next
        head = p.next
        p.next = None
        return head