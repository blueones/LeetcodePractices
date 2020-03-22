# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dictN = list()
        node = head
        while node != None:
            currentNode = node
            dictN.append(currentNode)
            node = node.next
        lenL = len(dictN)
        if 1< n < lenL:
            dictN[lenL -n-1].next = dictN[lenL-n+1]
            dictN[lenL-n].next = None
        elif n == lenL:
            return head.next
        elif n == 1:
            dictN[-2].next = None
        
        return head