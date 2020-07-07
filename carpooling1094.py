class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # trips.sort(key = lambda x:(x[1],x[2]))
        full_trip = {}
        for trip in trips:
            people, start, end = trip
            for i in range(start, end, 1):
                if i in full_trip:
                    full_trip[i] += people
                else:
                    full_trip[i] = people
                if full_trip[i] > capacity:
                    return False
        return True