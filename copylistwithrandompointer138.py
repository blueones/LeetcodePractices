
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #copy one by one, stop when for a node, the next is null
        def copynext(head2):
            dictO={}
            before=None
            returnh=before
            head1=head2
            num=0
            while head1!=None:
                headc=Node(head1.val)
                dictO[num]=head1.random
                num+=1
                if head1.random in listcreated:
                if head.next==None:
                    before.next=headc
                    headc.next=None
                elif head.next!=None:
                    before.next=headc
                    before=headc
                    head1=head1.next
            for node in dictO:

            return returnh.next
        newhead=copynext(head)



        