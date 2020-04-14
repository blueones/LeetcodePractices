class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count= 0
        count_dict = {0:[-1]}
        max_con = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            elif nums[i] == 1:
                count +=1
            if count in count_dict:
                if len(count_dict[count])==2:
                    count_dict[count][1]=i
                    
                else:
                    count_dict[count].append(i)
                max_con = max(max_con,i- count_dict[count][0])
            else:
                count_dict[count]= [i]
        print(count_dict)
        return max_con
        

        