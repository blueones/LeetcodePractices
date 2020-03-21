class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        index1 = index2 = 0
        resultL = []
        while index1<len1 and index2<len2:
            if nums1[index1]==nums2[index2]:
                resultL.append(nums1[index1])
                index1 += 1
                index2 += 1
            else:
                if nums1[index1]>nums2[index2]:
                    index2+=1
                else:
                    index1+=1
        return resultL
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1.sort() no sorting cause sorting takes O(nlog(n))
        # nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        if len1< len2:
            nums1,nums2 = nums2, nums1
        dictM = {}
        for num in nums2:
            if num in dictM:
                dictM[num]+=1
            else:
                dictM[num]=1
        replace = 0
        for num in nums1:
            if num in dictM and dictM[num]>0:
                nums1[replace]=num
                replace += 1
                dictM[num]-=1
        return nums1[:replace]
