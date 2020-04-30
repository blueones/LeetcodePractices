# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(before, node):
            if node == None:
                return before
            next_node = node.next
            node.next = before
            return helper(node, next_node)
        return helper(None, head)
class Solution1:
    def reverseList(self,head):
        #iterative
        current_node = None
        next_node = head
        while next_node!= None:
            new_next_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = new_next_node
        return current_node