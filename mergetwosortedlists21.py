# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        beforeN = ListNode(0)
        dummyN = beforeN
        if l1 == None and l2 == None:
            return None
        while l1 or l2:
            #print("here?")
            if l1 and l2:
                if l1.val >= l2.val:
                    beforeN.next = l2
                    l2 = l2.next
                else:
                    beforeN.next = l1
                    l1 = l1.next  
            elif l1 == None:
                beforeN.next = l2
                break
            elif l2 == None:
                beforeN.next = l1
                break
            beforeN = beforeN.next
        
        return dummyN.next
sunnyNode = ListNode(1)
sunnyNode2 = None
print(Solution().mergeTwoLists(sunnyNode,sunnyNode2))
