class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #TLE
        if m*k > len(bloomDay):
            return -1
        start_day = min(bloomDay)
        end_day = max(bloomDay)
        dates = set(bloomDay)
        list_dates = list(dates)
        list_dates.sort()
        bloom_ready = [0 for flower in bloomDay]
        
        for date in list_dates:
            target = 0
            for index in range(len(bloomDay)):
                if bloomDay[index] <= date:
                    if index == 0:
                        bloom_ready[index] = 1
                    elif bloom_ready[index-1] == k:
                        bloom_ready[index] = 1
                        
                    else:
                        bloom_ready[index] = bloom_ready[index-1] +1
               
                        
                
                if bloom_ready[index] == k:
                    target += 1
                    
            
            if target >= m:
                return date
        return -1
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #binary search. when searching, always think of binary search.
        if m*k > len(bloomDay):
            return -1
        start_day = min(bloomDay)
        end_day = max(bloomDay)
        dates = set(bloomDay)
        list_dates = list(dates)
        list_dates.sort()
        
        while start_day<= end_day:
            mid = (start_day+end_day)//2
            target = 0
            bloom_ready = [0 for flower in bloomDay]
            for index in range(len(bloomDay)):
                if bloomDay[index] <= mid:
                    if index == 0:
                        bloom_ready[index] = 1
                    elif bloom_ready[index-1] == k:
                        bloom_ready[index] = 1
                        
                    else:
                        bloom_ready[index] = bloom_ready[index-1] +1
              
                if bloom_ready[index] == k:
                    target += 1
            if target >= m:
                end_day = mid-1
            else:
                start_day = mid+1
        return start_day
                    