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

#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None or head.next == None or k < 2:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head != None:
            for i in range(1, k+1):
                if head.next == None:
                    break
                head = head.next
            if i == k:
                cur = pre.next
                head = pre.next.next
                for i in range(1, k):
                    tmp = head.next
                    cur.next = head.next
                    head.next = pre.next
                    pre.next = head
                    head = tmp
                pre = cur
                cur.next = head
            else:
                break
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
    linked = s.reverseKGroup(generateLinkedList([1,2,3,4]),2)
    printLinkedList(linked)