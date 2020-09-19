# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        pseudo = ListNode(0)
        current = pseudo
        while l1 or l2 or carry!= 0:
            value1 = value2 = 0
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next
            add_up = value1+value2+carry
            current_node = ListNode(add_up%10)
            current.next = current_node
            current = current.next
            carry = add_up//10
        return pseudo.next


# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Constraints:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency = {}
        for character in s1:
            if character in frequency:
                frequency[character] += 1
            else:
                frequency[character] = 1
        current_frequency = frequency.copy()
        start_index = 0
        next_index = 0
        while next_index < len(s2):
            if s2[next_index] in current_frequency:
                current_frequency[s2[next_index]] -= 1
                if current_frequency[s2[next_index]] < 0:
                    current_frequency = frequency.copy()
                    start_index += 1
                    next_index = start_index
                else:
                    if len(s1) == (next_index - start_index) + 1:
                        return True
                    next_index += 1
            else:
                current_frequency = frequency.copy()
                start_index += 1
                next_index = start_index
        return False





