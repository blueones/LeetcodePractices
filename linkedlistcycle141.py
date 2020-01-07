# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    #use hashtable to remember visited nodes
    def hasCycle(self, head: ListNode) -> bool:
        visited=list()
        while head!=None:
            if head in visited:
                return True
            else:
                visited.append(head)
                head=head.next
        return False

        

class Solution2:
    #two pointers, a fast runner and a slower runner. 
    # if they are running on a cycle, fast runner will eventually catch up with slower runner again. 
    def hasCycle(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return False
        fastR=head
        slowR=head
        while fastR!=None and fastR.next!=None:
            fastR=fastR.next.next
            slowR=slowR.next
            if fastR==slowR:
                return True
        return False
    
class Solution3:
    #tiny improvement on Solution2. have fast runner take one step ahead first. 
    def hasCycle(self, head: ListNode) -> bool:
        try:
            fastR=head.next
            slowR=head
            while fastR!=None:
                if fastR==slowR:
                    return True
                fastR=fastR.next.next
                slowR=slowR.next
        except:    
            return False