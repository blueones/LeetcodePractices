class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #find the target array
        #find how many digits are different from the target array
        target_array = sorted(heights)
        len_heights = len(heights)
        counts = 0
        for i in range(len_heights):
            if target_array[i]!= heights[i]:
                counts +=1
        return counts