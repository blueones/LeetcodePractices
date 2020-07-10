class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit),key = lambda x:x[1])
        dp = [[0, 0]]
        def find_biggest(start_time):
            start = 0
            end = len(dp)
            while start < end:
                mid = (start+end)//2
                if dp[mid][0]<= start_time:
                    start = mid+1
                else:
                    end = mid
            return start-1
        for i in range(len(jobs)):
            start, end, profit = jobs[i]
            #find dp[at some time] where it's endtime is smaller or equal to start
            find_in_dp = find_biggest(start)
            if find_in_dp == -1:
                available_pre_profit = 0
            else:
                available_pre_profit = dp[find_in_dp][1]
            new_profit = max(dp[-1][1], available_pre_profit+profit)
            dp.append([end, new_profit])
        return dp[-1][1]