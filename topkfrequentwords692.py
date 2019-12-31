class Solution:
    def topKFrequent(self, words, k) :
        words.sort()
        wordDict={}
        for word in words:
            if word not in wordDict:
                wordDict[word]=1
            else:
                wordDict[word]+=1
        numDict={}
        for numword in wordDict:
            if wordDict[numword] not in numDict:
                numDict[wordDict[numword]]=[numword]
            else:
                numDict[wordDict[numword]].append(numword)
        numL=[i for i in numDict]
        numL.sort(reverse=True)
        counter=0
        resultL=[]
        for num in numL:
            numDict[num].sort()
            for wordN in numDict[num]:
                resultL.append(wordN)
                counter+=1
                if counter==k:
                    return resultL

print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))
        