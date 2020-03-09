class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resultL = []
        lenN = len(nums)
        def DFS(focus):
            if focus == lenN:
                resultL.append(nums[:])
            else:
                for i in range(focus, lenN, 1):
                    nums[i],nums[focus]= nums[focus], nums[i]
                    DFS(focus+1)
                    nums[i],nums[focus]= nums[focus], nums[i]
        DFS(0)
        return resultL