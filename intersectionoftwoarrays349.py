class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictShare = {}
        for num in nums1:
            dictShare[num]=1
        for num2 in nums2:
            if num2 in dictShare:
                dictShare[num2]=2
        resultL = []
        for key in dictShare:
            if dictShare[key]==2:
                resultL.append(key)
        return resultL
class Solution1:
    def intersection(self,nums1,nums2):
        #two pointers
        len1 = len(nums1)
        len2 = len(nums2)
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        while i<len1 and j <len2:
            if nums1[i]==nums2[j]:
                if not (res and res[-1]== nums1[i]):
                    res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
        return res