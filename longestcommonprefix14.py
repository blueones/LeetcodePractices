class Solution:
    def longestCommonPrefix(self, strs):
        self.strs = strs
        lenS = len(strs)
        if lenS == 0:
            return ""
        shared = strs[0]
        sharedD = len(shared)
        n = 1
        while n < lenS:
            lenC = len(self.strs[n])
            sharedD = min(sharedD,lenC)
            shared = shared[:sharedD]
            for i in range(sharedD):
                if shared[i]!= self.strs[n][i]:
                    sharedD = i
                    shared = shared[:i]
                    break
            n+=1
        return shared
            
            
                
