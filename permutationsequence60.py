class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #the very proof that I am a genius.
        resultS = ""
        stringO = ""
        for i in range(1,n+1):
            stringO+=str(i)
        n=n-1
        k=k-1
        while n>0:
            index = k//(math.factorial(n))
            k = k%(math.factorial(n))
            resultS+= stringO[index]
            stringO=stringO[:index]+stringO[index+1:]
            n -= 1
        
        resultS += stringO[0]

        return resultS