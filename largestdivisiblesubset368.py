class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        largest = (0,1)
        nums.sort()
        subset_length = [(1, [nums[i]]) for i in range(len(nums))]
        subset_length[0] = (1, [nums[0]])

        for index in range(len(nums)):
            local_largest = 1
            for j in range(index-1, -1, -1):
                if nums[index]%nums[j] == 0:
                    if subset_length[j][0] +1 > local_largest:
                        character_list = subset_length[j][1].copy()
                        character_list.append(nums[index])
                        subset_length[index] = (subset_length[j][0]+1, character_list)
                        local_largest = subset_length[j][0]+1

                        if subset_length[index][0] > largest[1]:
                            largest = (index, subset_length[index][0])
        print(subset_length)
        return subset_length[largest[0]][1]
        
            