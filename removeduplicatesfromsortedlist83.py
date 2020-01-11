# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def delete(head,beforeN):
            if head == None:
                return None
            else:
                if beforeN!= None and head.val==beforeN.val:
                    nodeN = head.next
                    beforeN.next = nodeN
                    delete(nodeN,beforeN)
                else:
                    delete(head.next,head)
        nodeC = head
        delete(nodeC,None)
        return head

class Solution2:
    def deleteDuplicates(self,head):
        nodeC = head
        beforeN = None
        while nodeC != None:
            if beforeN !=None and nodeC.val == beforeN.val:
                nodeN = nodeC.next
                beforeN.next = nodeN
            else:
                beforeN = nodeC
            nodeC = nodeC.next
                
        return head