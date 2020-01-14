class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # error prune solution. 
        dictVisited=dict()
        lenS = len(s)
        longestSub = 0 #always record the largest length of nonrepeating substring while traversing
        markBeginning = 0 # mark the beginning of current traversed nonrepeating substring. 
                           # when bump into visited string, markbeginning will jump to the node next to the earlier visited node
        currentL = 0 # mark the length of current nonrepeating substring
        if s == None:
            return 0
        for i in range(0, lenS, 1):
            if s[i] in dictVisited:
                if dictVisited[s[i]] > markBeginning-1:
                    markBeginning = dictVisited[s[i]] + 1
                currentL = i - markBeginning + 1
                dictVisited[s[i]] = i
            elif s[i] not in dictVisited:
                dictVisited[s[i]] = i
                currentL += 1
            if currentL > longestSub:
                longestSub = currentL
            print(currentL ," is currentL")
            print(markBeginning, " is beginning")
        return longestSub
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window solution. Solution3 is way more clear but not as efficient.
        begin = 0
        end = 0
        largest = 0
        lenS = len(s)
        visitedDict = dict()
        for i in range(0, lenS, 1):
            if s[i] in visitedDict:
                
                if begin <= visitedDict[s[i]]:
                    begin = visitedDict[s[i]] + 1
                visitedDict[s[i]] = i
                end += 1
            elif s[i] not in visitedDict:
                visitedDict[s[i]] = i
                end += 1
            print("begin is ", begin, "end is ", end, "visitedDict is ", visitedDict)
            if largest < end - begin:
                largest = end - begin
        return largest
            
class Solution3:
    def lengthOfLongestSubstring(self, s):
        # sliding window issue.  keep sliding beginning to right until there are no duplicate letters in dictionary. keep deleting. 
        begin = 0
        end = 0
        largest = 0
        lenS = len(s)
        visitedDict = dict()
        while begin < lenS and end < lenS:
            if s[end] not in visitedDict:
                visitedDict[s[end]] = end
                end += 1
            elif s[end] in visitedDict:
                del visitedDict[s[begin]]
                begin += 1
            largest = max(largest, end - begin)
        return largest
                   
print(Solution2().lengthOfLongestSubstring('abcabcbb'))
        
        