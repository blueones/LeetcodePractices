# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #first do a reverselinkedlist
        #then compare one by one
        ### This solution is wrong since it changed the original list, 
        ##instead of creating a new one. reverselinkedlist is changing original list!!!!!

        if head==None:
            return True
        def reverselinkedlist(head1,before):
            if head1.next==None:
                head1.next=before
                return head1
            else:
                node=head1.next
                head1.next=before
                return reverselinkedlist(node,head1)
        node=head   
        reversedlist=reverselinkedlist(node,None)
        print(head.next)
        while head!=None and reversedlist!=None:
            if head.val!=reversedlist.val:
                return False
            head=head.next
            reversedlist=reversedlist.next
            print(head,reversedlist)
        if head==reversedlist:
            return True

class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        #first do a reverselinkedlist
        #then compare one by one
        ### This solution is going to create a new list at a new location for each node. 

        if head==None:
            return True
        def reverselinkedlist(head1):
            beforeNode=None
            while head1!=None:
                newNode=ListNode(head1.val)
                newNode.next=beforeNode
                beforeNode=newNode
                head1=head1.next
            return beforeNode  
        reversedlist=reverselinkedlist(head)
        while head!=None and reversedlist!=None:
            if head.val!=reversedlist.val:
                return False
            head=head.next
            reversedlist=reversedlist.next
        if head==reversedlist:
            return True
class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
sunnyNode=ListNode(1)
sunnyNode.next=ListNode(0)
sunnyNode.next.next=ListNode(1)
print(Solution2().isPalindrome(sunnyNode))