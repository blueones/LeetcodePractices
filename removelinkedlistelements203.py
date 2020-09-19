# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #look through the list
        # if val is val, then do something
        # if val is not, then move on with the linkedlist
        # what needs to be done with deleting an element. this is similiar with reverselist really. we need to always know the before. 
        self.target=val
        def remove(head):
            before=None
            nodeH=head
            while nodeH!=None:
                if nodeH.val==self.target:
                    
                    
                    nodeH=nodeH.next
                    if before!=None:
                        before.next=nodeH
                    elif before==None:
                        head=nodeH
                else:
                    #print(nodeH.val,"You are okay")
                    node=nodeH
                    nodeH=nodeH.next
                    before=node       
            return head
        newhead=remove(head)
        return newhead.val
sunnyNode=ListNode(1)
sunnyNode.next=ListNode(2)
sunnyNode.next.next=ListNode(6)
sunnyNode.next.next.next=ListNode(3)
sunnyNode.next.next.next.next=ListNode(4)
sunnyNode.next.next.next.next.next=ListNode(5)
sunnyNode.next.next.next.next.next.next=ListNode(6)
print(Solution().removeElements(sunnyNode,6))            
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        pseudo_head = ListNode(0)
        pseudo_head.next = head
        current = head
        before = pseudo_head
        while current != None:
            if current.val == val:
                before.next = current.next
                
                current.next = None
                current = before.next
                
            else:
            
                before = before.next
                current = current.next
        return pseudo_head.next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        pseudo_head = ListNode(0)
        pseudo_head.next = head
        current = head
        before = pseudo_head
        while current != None:
            if current.val == val:
                before.next = current.next
                
                
                
                
            else:
            
                before = before.next
            current = current.next
        return pseudo_head.next0
                    
        
