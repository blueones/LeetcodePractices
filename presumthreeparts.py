#input: input_list
#output: how many ways to seperate this list into three partitions so that each partition is smaller or equal to the next one. 
class Solution:
    def partition_three_parts(self, input_list):
        #calculate total
        total = sum(input_list)
        # calculate max_sum of first partition.
        partitioned = total//3
        tmp = 0
        for i,num in enumerate(input_list):
            tmp += num
            if tmp> partitioned:
                break
        #first partition is at most at index first
        first = i-1
        # dp = [False for i in range()]