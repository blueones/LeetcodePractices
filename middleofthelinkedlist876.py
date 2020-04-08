# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        fast_runner = dummy_node
        slow_runner = dummy_node
        while fast_runner.next and fast_runner.next.next:
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next
        return slow_runner.next