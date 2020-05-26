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
        
class Solution1:
    def findMaxLength(self, nums: List[int]) -> int:
        #no need to save the latter index as you did in solution.
        count= 0
        count_dict = {0:-1}
        max_con = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            elif nums[i] == 1:
                count +=1
            if count in count_dict:
                
                max_con = max(max_con,i- count_dict[count])
            else:
                count_dict[count]= i
        return max_con
class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        num_sum = [0]
        for num in nums:
            if num == 1:
                num_sum.append(num_sum[-1]+1)
            elif num == 0:
                num_sum.append(num_sum[-1]-1)
        dict_sum = {}
        for index in range(len(num_sum)):
            if num_sum[index] in dict_sum:
                dict_sum[num_sum[index]].append(index)
            else:
                dict_sum[num_sum[index]] = [index]
        length_list = [dict_sum[i][-1]- dict_sum[i][0] for i in dict_sum]
        return max(length_list)
        

        
        