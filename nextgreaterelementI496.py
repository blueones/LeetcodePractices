class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        result_nums1 = []
        for num1 in nums1:
            index1 = nums2.index(num1)
            found = False
            for num2 in range(index1,len2):
                if nums2[num2]>num1:
                    result_nums1.append(nums2[num2])
                    found = True
                    break
            if not found:
                result_nums1.append(-1)
        return result_nums1
class Solution1:
    def nextGreaterElement(self,nums1,nums2):
        dict_next_greater_nums2 = dict()
        len2 = len(nums2)
        resultL = []
        for index2 in range(len2):
            for i in range(index2,len2):
                if nums2[i]>nums2[index2]:
                    dict_next_greater_nums2[nums2[index2]] = nums2[i]
                    break
            if nums2[index2] not in dict_next_greater_nums2:
                dict_next_greater_nums2[nums2[index2]]=-1
        for num1 in nums1:
            resultL.append(dict_next_greater_nums2[num1])
        return resultL
class Solution2:
    def nextGreaterElement(self,nums1,nums2):
        dict_next_greater_nums2= {}
        len2 = len(nums2)
        stack = []
        resultL = []
        for index2 in range(len2):
            while stack and nums2[index2]> stack[-1]:
                dict_next_greater_nums2[stack.pop(-1)]= nums2[index2]
            stack.append(nums2[index2])
        for item_left in stack:
            dict_next_greater_nums2[item_left]=-1
        for num1 in nums1:
            resultL.append(dict_next_greater_nums2[num1])
        return resultL