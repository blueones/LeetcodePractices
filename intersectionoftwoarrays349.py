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