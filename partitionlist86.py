# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: #wrong solution!!!!!!
    def partition(self, head: ListNode, x: int) -> ListNode:
        #think about quicksort issue
        #partition = 0 
        # 
        # #everything to the left of partition is smaller than x which is the pivot value
        # traverse thru the linked list. when traverse.val < pivot(x), move partition one more right, 
        #and traverse to the next one, when traverse.val > pivot, 
        # keep traversing until meet traverse .val < pivot then swap the value on partion with the value on traverse
        # ends when traverse reach the end of linked list.
        #
        #traverse = 0 
        #remember to work on the swapping of the nodes instead of just values. since we want to keep preserving the original relative order of the nodes. 
        nodeH = head
        partition = head
        fakehead = ListNode(0)
        fakehead.next = head
        nodeHprevious = partitionprevious = fakehead

        while nodeH != None:
            if nodeH.val < x:
                #swap node partition and nodeH
                nodeHnext = nodeH.next
                partitionprevious.next = nodeH
                nodeHprevious.next = nodeHnext
                nodeH.next = partition
                partition = partition.next
                partitionprevious = partitionprevious.next
            nodeH = nodeH.next
            nodeHprevious = nodeHprevious.next
        return head
                
class Solution1:
    def partition(self,head, x):
        #use before and after to create two linked list
        #then tie two linked list together. 
        #remember this easy and simple trick. 
        nodeBefore = dummyBefore = ListNode(0)
        nodeAfter = dummyAfter = ListNode(0)
        if head == None:
            return None
        while head != None:
            nodeNext = head.next
            if head.val < x:
                nodeBefore.next = head
                nodeBefore = nodeBefore.next
            elif head.val >= x:
                nodeAfter.next = head
                nodeAfter = nodeAfter.next
            head.next = None
            head = nodeNext
        nodeBefore.next = dummyAfter.next
        dummyAfter.next = None
        returnNode = dummyBefore.next
        dummyBefore.next = None
        return returnNode