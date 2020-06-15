import heapq
class Solution:
    #dijkastra solution. Greedy. be mindful of line 20. why is it correct. brilliant
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dict_flights = {}
        for flight in flights:
            start, end, price = flight
            if start in dict_flights:
                dict_flights[start].append((end, price))
            else:
                dict_flights[start] = [(end, price)]
        

        #price, current, stops
        heap = [(0, src, 0)]
        
        while heap:
            price, current_loc, stops = heapq.heappop(heap)
            if current_loc == dst:
                return price
            else:
                if stops <= K:
                    if current_loc in dict_flights:
                        for next_loc, cost in dict_flights[current_loc]:
                            heapq.heappush(heap, (price+cost, next_loc, stops+1))
                    
        return -1
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        #used visited set to record visited on each path to avoid cycles. but not good enough. 
        dict_flights = {}
        for flight in flights:
            start, end, price = flight
            if start in dict_flights:
                dict_flights[start].append([end, price])
            else:
                dict_flights[start] = [[end, price]]
        self.min_price = float("inf")
        
        def find_path(current_city, current_stops, current_price, visited):
            
            if current_city == dst:
                if current_stops <= K+1:
                    self.min_price = min(self.min_price, current_price)
            elif current_stops < K+1:
              
                    if current_city in dict_flights:
                        available_dst = dict_flights[current_city]
                        for dst_next, price in available_dst:
                            if dst_next not in visited:
                                visited.add(dst_next)
                                find_path(dst_next, current_stops+1, price+ current_price, visited)
                                visited.remove(dst_next)
        visited = set()
        visited.add(src)
        find_path(src, 0, 0, visited)
        return self.min_price if self.min_price != float("inf") else -1
            
            