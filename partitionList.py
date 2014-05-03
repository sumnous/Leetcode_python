#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-3
@author: Ting Wang
'''

#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.
#For example,
#Given 1->4->3->2->5->2 and x = 3,
#return 1->2->2->4->3->5.

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return head
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before = before_dummy
        after = after_dummy
        while head != None:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next
        before.next = after_dummy.next
        after.next = None
        return before_dummy.next

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
    result = s.partition(generateLinkedList([2,1]),2)
    printLinkedList(result)

