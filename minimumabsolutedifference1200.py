class Solution:
    def minimumAbsDifference(self, arr):
        diff=dict()
        length=len(arr)
        arr.sort()
        resultL=list()

        for i in range(0,length-1,1):
            diff[i]=abs(arr[i]-arr[i+1])
        minD=min(diff.values())
        for i in range(0,length-1):
            if diff[i]==minD:
                resultL.append([arr[i],arr[i+1]])
        return resultL
Solution().minimumAbsDifference([4,2,1,3])
        
