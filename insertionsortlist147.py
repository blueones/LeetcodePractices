# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #inplace
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()
        pseudo_head.next = head
        pointer = head
        pointer_prior = pseudo_head
        while pointer:
            replacement = pseudo_head.next
            replacement_prior = pseudo_head
            while replacement!= pointer and replacement.val<= pointer.val:
                replacement_prior = replacement
                replacement = replacement.next
            if replacement != pointer:
                replacement_prior.next = pointer
                temp_pointer_next = pointer.next
                pointer.next = replacement
                pointer = temp_pointer_next
                pointer_prior.next = pointer
            else:
                pointer_prior = pointer
                pointer = pointer.next
            
        return pseudo_head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    #create a new list, go thru original list and append nodes from original list into new list.
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()
        pointer = head
        while pointer:
            
            iterator_prior = pseudo_head
            iterator = iterator_prior.next
            while iterator and iterator.val<= pointer.val:
                iterator_prior = iterator
                iterator = iterator.next
            iterator_prior.next = pointer
            temp_next = pointer.next
            pointer.next = iterator
            pointer = temp_next
            
            
            
            
        return pseudo_head.next
        