class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse = True)