from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        product = [[0 for i in range(len(nums2))] for j in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                product[i][j] = nums1[i]*nums2[j]
        self.max_product = product[0][0]
        @lru_cache
        def backtracking(index1,index2):
            current_product = []
            for i in range(index1, len(nums1)):
                for j in range(index2, len(nums2)):
                    current_product1 = product[i][j] + backtracking(i+1, j+1)
                    self.max_product = max(self.max_product, current_product1, product[i][j])
                    current_product.append(current_product1)
                    current_product.append(product[i][j])
            if current_product:
                return max(current_product)
            return 0
        backtracking(0,0)
        return self.max_product
class Solution1:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float("-inf") for j in range(len(nums2)+1)]for i in range(len(nums1)+1)]
        # for i in range(len(nums1)):
        #     dp[i][len(nums2)-1] = nums1[i] * nums2[len(nums2)-1]
        # for j in range(len(nums2)):
        #     dp[len(nums1)-1][j] = nums1[len(nums1)-1]* nums2[j]
        for i in range(len(nums1)-1, -1, -1):
            for j in range(len(nums2)-1, -1, -1):
                dp[i][j] = max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]+ nums1[i]*nums2[j], nums1[i]*nums2[j], dp[i+1][j+1] )
        return dp[0][0]
        
        