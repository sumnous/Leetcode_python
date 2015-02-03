# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB
        if headA == None or headB == None:
            return
        while pA and pB:
            print pA.val, pB.val
            if pA.val != pB.val:
                if pA.next and pB.next:
                    pA = pA.next
                    pB = pB.next
                elif pA.next == None and pB.next != None:
                    pA = headB
                    pB = pB.next
                elif pB.next == None and pA.next != None:
                    pB = headA
                    pA = pA.next
                else:
                    return
            else:
                return pA.val


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
    #linked1 = generateLinkedList([1,3,5,7,9,11])
    #linked2 = generateLinkedList([2,4,9,11])
    linked1 = generateLinkedList([1])
    linked2 = generateLinkedList([1])
    print s.getIntersectionNode(linked1,linked2)