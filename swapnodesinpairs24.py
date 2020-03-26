# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        nodeLead = dummy
        while nodeLead:
            node1 = nodeLead.next
            if node1:
                node2 = node1.next
                if node2:
                    node3 = node2.next
                    nodeLead.next = node2
                    node2.next = node1
                    node1.next = node3
                    nodeLead = node1
                else:
                    break
            else:
                break
        return dummy.next
