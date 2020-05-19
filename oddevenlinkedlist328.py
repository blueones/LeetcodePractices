# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = head
        dummy_even = ListNode(0)
        even_head = dummy_even
        odd_current = odd_head
        even_current = even_head
        while odd_current:
            if odd_current.next:
                even = odd_current.next
                
                even_current.next = even
                even_current = even_current.next
                if odd_current.next.next:
                    odd_next = odd_current.next.next
                    even.next = None
                    odd_current.next = odd_next
                    odd_current = odd_current.next
                else:
                    break
            else:
                break
        if odd_current:
            odd_current.next = dummy_even.next
        return odd_head
        
            