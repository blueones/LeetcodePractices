from functools import lru_cache
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        @lru_cache(None)
        def find(index, unlocated_mailboxes, last_mailbox):
            if index == len(houses):
                return 0
            else:
                distance = 0
                if unlocated_mailboxes == 0:
                    for i in range(index, len(houses)):
                        distance += abs(houses[i] - last_mailbox)
                    return distance
                else:
                    distance = float("inf")

                    for i in range(index,len(houses)):
                        #put next mailbox here at i
                        part_distance = 0
                        if last_mailbox != None:
                            for j in range(index, i+1):
                                part_distance += min(abs(houses[j] - houses[i]), abs(last_mailbox - houses[j]))
                        total_distance = part_distance + find(i, unlocated_mailboxes-1, houses[i])
                        distance = min(distance, total_distance)
                    return distance
        total = float("inf")
        for i in range(len(houses)):
            #put mailbox at i
            distance = 0
            for j in range(i+1):
                distance += abs(houses[i]-houses[j])
            total = min(total, distance + find(i+1, k-1, houses[i]))
        return total
            