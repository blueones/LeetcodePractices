# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #brute force O(m*n)
        while headA!=None:
            node=headB
            while node!=None:
                if headA==node:
                    return node
                node=node.next
            headA=headA.next
        return None
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #still brute force, O(m+n)
        dictA=list()
        while headA!=None:
            dictA.append(headA)
            headA=headA.next
        while headB!=None:
            if headB in dictA:
                return headB
            headB=headB.next
        return None
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #two pointer. O(m+n), space complexity though is only O(1), solution2 has an headA array which take up O(m).
        nodeA=headA
        nodeB=headB
        switchFlagA=False
        switchFlagB=False
        while nodeA!=None and nodeB!=None:
            if nodeA==nodeB:
                return nodeA
            nodeA=nodeA.next
            nodeB=nodeB.next
            if nodeA==None and switchFlagA==False:
                nodeA=headB
                switchFlagA=True
            if nodeB==None and switchFlagB==False:
                nodeB=headA
                switchFlagB=True
        return None