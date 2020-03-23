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
class Solution3:
    # same intuition as solution2, but with two pointers doing one scan. 
    # have fast pointer start from n+1, and slow pointer start from 0. then have them both start going one node at a time. 
    # eventually, fast pointer goes to the end which is a None node, 
    # and slow pointer is at n+1 from this None node. which is a node before our takeout node.
    def removeNthFromEnd(self,head,n):
        dummy = TreeNode(0)
        dummy.next = head
        faster = dummy
        slower = dummy
        fastM = 0
        slowM = 0
        while fastM<n+1:
            faster = faster.next
            fastM += 1
        while faster != None:
            faster = faster.next
            slower = slower.next
            fastM += 1
            slowM += 1
        slower.next = slower.next.next
        return dummy.next
class Solution4:
    # clean up solution3.
    def removeNthFromEnd(self,head,n):
        dummy = TreeNode(0)
        dummy.next = head
        faster = dummy
        slower = dummy
        fastM = 0
        # slowM = 0
        # while fastM<n+1:
        #     faster = faster.next
        #     fastM += 1
        for i in range(n+1):
            faster= faster.next
        while faster != None:
            faster = faster.next
            slower = slower.next
            # fastM += 1
            # slowM += 1
        slower.next = slower.next.next
        return dummy.next



            

          

