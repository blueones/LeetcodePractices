class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_dict = {}
        for task in tasks:
            if task in frequency_dict:
                frequency_dict[task] += 1
            else:
                frequency_dict[task] = 1
        task_sorted = sorted(frequency_dict, reverse = True,key = lambda x:frequency_dict[x])
        dict_put = defaultdict(list)
        max_i = 0
        for task in task_sorted:
            for i in range(frequency_dict[task]):
                
                if len(dict_put[i]) < n+1:
                    dict_put[i].append(task)
                    max_i = max(max_i,i)
                elif len(dict_put[i]) == n+1:
                    while len(dict_put[i])==n+1:
                        i+= 1

                    dict_put[i].append(task)

                    max_i =max(max_i, i)
                
        return (max_i)*(n+1)+len(dict_put[max_i]) 