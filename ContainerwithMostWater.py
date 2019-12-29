class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        maxA=min(height[i],height[j])*(j-i)
        newArea=maxA
        #print (maxA)
        while i<j:
            if height[i]>=height[j]:
                
                if newArea<=maxA and i<j:
                    j=j-1
                    newArea=min(height[i],height[j])*(j-i)
                    if newArea>maxA:
                        maxA=newArea
                        print("i now is",i,"j now is",j,"maxA now is",maxA)
                
            elif height[i]<height[j]:
                
                if newArea<=maxA and i<j:
                    print("hello")
                    i=i+1
                    newArea=min(height[i],height[j])*(j-i)
                    print("i now is",i,"j now is",j,"maxArea now is",newArea)
                    if newArea>maxA:
                        maxA=newArea
                        #print("hello")
                        print("i now is",i,"j now is",j,"maxA now is",maxA)
            continue
        return maxA
print(Solution().maxArea([6,14,2,11,2,7,0,9,12,7]))

        