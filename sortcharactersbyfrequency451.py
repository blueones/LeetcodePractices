class Solution:
    def frequencySort(self, s: str) -> str:
        dict_frequency = {}
        for cha in s:
            if cha in dict_frequency:
                dict_frequency[cha] += 1
            else:
                dict_frequency[cha] = 1
        sorted_frequency = sorted(dict_frequency, reverse = True, key = lambda x:dict_frequency[x])
        list_sorted = [i*dict_frequency[i] for i in sorted_frequency]
        return "".join(list_sorted)
class Solution1:
    def frequencySort(self, s):
        #bucket sort, notice how we don't care about whether in tree, t go before r or r go before t.
        #so we can sort based on frequency. put each frequency of list of words into a bucket.
        # thus we traverse our list and get O(n) time complexity, instead of klog(k). 
        #which method is better depends on n and k value
        if s == "":
            return ""
        dict_frequency = {}
        for cha in s:
            if cha in dict_frequency:
                dict_frequency[cha] += 1
                
            else:
                dict_frequency[cha] = 1
        max_frequency = max(dict_frequency.values())
        frequency_list = [[] for i in range(max_frequency)]
        for cha in dict_frequency:
            frequency_list[dict_frequency[cha]-1].append(cha)
        list_letters = []
        for i in range(max_frequency-1,-1, -1):
            for word in frequency_list[i]:
                list_letters.append(word*(i+1))
        return "".join(list_letters)
class Solution2:
    def frequencySort(self, s):
        #syntax candy solution
        