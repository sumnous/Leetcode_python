#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-02
@author: Ting Wang
'''

#Reverse a linked list from position m to n. Do it in-place and in one-pass.
#For example:
#Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#return 1->4->3->2->5->NULL.
#Note:
#Given m, n satisfy the following condition:
#1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(1,n+1):
            if i == m:
                prev_m = prev
            if i > m and i <= n:
                prev.next = head.next
                head.next = prev_m.next
                prev_m.next = head
                head = prev
            prev = head
            head = head.next
        return dummy.next

def generateLinkedList(array):
    if len(array) == 0:
        return None
    head = ListNode(array[0])
    curr = head
    for i in range(1, len(array)):
        node = ListNode(array[i])
        curr.next = node
        curr = node
    return head

def printLinkedList(curr):
    result = []
    while curr != None:
        result.append(curr.val)
        curr = curr.next
    print(result)

if __name__ == '__main__':
    s = Solution()
    linked = s.reverseBetween(generateLinkedList([3,5]),1,2)
    printLinkedList(linked)