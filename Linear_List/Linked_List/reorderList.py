#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-18
@author: Ting Wang
'''

#Given a singly linked list L: L0→L1→…→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#You must do this in-place without altering the nodes' values.
#For example,
#Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        prev = None
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        slow = self.reverse(slow)
        cur = head
        while cur.next != None:
            tmp = cur.next
            cur.next = slow
            slow = slow.next
            cur.next.next = tmp
            cur = tmp
        cur.next = slow
        return cur
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        head = head.next
        while head != None:
            cur.next = head.next
            head.next = prev.next
            prev.next = head
            head = cur.next
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
    linked = s.reorderList(generateLinkedList([1,2,3]))
    printLinkedList(linked)