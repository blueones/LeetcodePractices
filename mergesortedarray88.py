class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = 0
        pointer2 = 0
        nums1_copy = nums1[:m].copy()
        for index in range(m+n):
            if pointer1 == m:
                nums1[index] = nums2[pointer2]
                pointer2 += 1
            elif pointer2 == n:
                nums1[index] = nums1_copy[pointer1]
                pointer1 += 1
                
            elif nums1_copy[pointer1] <= nums2[pointer2]:
                nums1[index] = nums1_copy[pointer1]
                pointer1 += 1
            elif nums1_copy[pointer1] > nums2[pointer2]:
                nums1[index] = nums2[pointer2]
                pointer2 += 1
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #merge into nums1 from the end, so avoid creating extra space. 
        pointer1 = m-1
        pointer2 = n-1
        for index in range(m+n-1, -1, -1):
            if pointer1 == -1:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
            elif pointer2 == -1:
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
            elif nums1[pointer1] >= nums2[pointer2]:
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
            elif nums1[pointer1] < nums2[pointer2]:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m-1
        pointer2 = n-1
        pointer = m+n-1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer] = nums2[pointer2]
                pointer2 -= 1
            pointer -= 1
        nums1[:pointer2+1] = nums2[:pointer2+1]
                
        