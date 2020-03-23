# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#could use DummyNode to care for corner cases. 
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #algorithm: to put every node that we pass into a list.
        # time complexity: O(N)
        # space complexity: O(N)
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
class Solution1:
    def removeNthFromEnd(self,head,n):
        #two passes
        # one pass to count number of nodes
        # one pass to go to lenL - n
        dummy = TreeNode(0)
        dummy.next = head
        node = dummy
        marker = -1
        while node != None:
            marker +=1
            node = node.next
        lenN = marker
        #find (lenN - n+1)th node which is
        newMarker = 0
        node = dummy
        while newMarker < lenN-n:
            newMarker+=1
            node = node.next
        takenoutNode = node.next
        followNode = takenoutNode.next
        node.next = followNode
        if takenoutNode != None:
            takenoutNode.next = None
        return dummy.next
class Solution2:
    def removeNthFromEnd(self,head,n):
        #revise solution1
        #no need to count dummy when doing counting
        # no need to make the deleted node.next = None
        #be careful with markers. It could be error prone.
        dummy = TreeNode(0)
        dummy.next = head
        #to count
        lenN = 0
        node = head
        while node != None:
            lenN+=1
            node = node.next
        lenN -= n
        node = dummy
        while lenN>0:
            lenN -= 1
            node= node.next
        node.next = node.next.next
        return dummy.next
            

          

