class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances_dict = {}
        paired = dict()
        worker_pair = defaultdict(set)
        bike_pair = defaultdict(set)
        ans = [None for i in range(len(workers))]
        for index_w, worker in enumerate(workers):
            for index_b, bike in enumerate(bikes):
                manhattan = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                if manhattan not in distances_dict:
                    distances_dict[manhattan] = deque()
                distances_dict[manhattan].append((index_w, index_b))
                paired[(index_w, index_b)] = False
                worker_pair[index_w].add((index_w, index_b))
                bike_pair[index_b].add((index_w, index_b))
        for distance in sorted(distances_dict):
            while distances_dict[distance]:
                worker, bike = distances_dict[distance].popleft()
                if paired[(worker, bike)] == False:
                    paired[(worker, bike)] = True
                    ans[worker] = bike
                    for pair in worker_pair[worker]:
                        paired[pair] = True
                    for pair in bike_pair[bike]:
                        paired[pair] = True
        return ans