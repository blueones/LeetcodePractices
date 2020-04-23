# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        carry = 0
        currentNode = dummy
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            current_sum = carry+num1+num2
            
            currentNode.next = ListNode(current_sum%10)
            currentNode = currentNode.next

            carry = current_sum//10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry != 0:
            newNode = ListNode(carry)
            currentNode.next = newNode
        return dummy.next