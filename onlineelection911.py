class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons_array = list()
        count = dict()
        current_lead, current_count = None, 0
        for index in range(len(times)):
            if persons[index] in count:
                count[persons[index]] += 1
            else:
                count[persons[index]] = 1
            if count[persons[index]] >= current_count:
                current_lead = persons[index]
                current_count = count[persons[index]]
            self.persons_array.append(current_lead)
            
                

    def q(self, t: int) -> int:
        def find(t):
            start = 0
            end = len(self.times)-1
            while start <= end:
                mid = (start+end)//2
                if self.times[mid] ==t:
                    return mid
                elif self.times[mid]>t:
                    end = mid-1
                    
                else:
                    start = mid+1
            return end
        index = find(t)
        return self.persons_array[index]
