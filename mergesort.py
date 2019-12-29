import math

def mergesort(aList):
    if len(aList)>2:
        middle=math.ceil(len(aList)/2)
        #print("middle number is",middle)
        leftList=aList[:middle]
        rightList=aList[middle:]
        orderedLeft=mergesort(leftList)  
        #print ("orderedLeft list is",orderedLeft)       
        orderedRight=mergesort(rightList)
        combinedList=[]
        i=j=0
        while i<len(orderedLeft) or j<len(orderedRight):
            if i==len(orderedLeft):
                #print("combinedList is",combinedList, "and i is ",i, "j is",j)
                combinedList.append(orderedRight[j])
                j+=1
            elif j==len(orderedRight):
                combinedList.append(orderedLeft[i])
                i+=1
            elif orderedLeft[i]<=orderedRight[j]:
                combinedList.append(orderedLeft[i])
                i+=1
            elif orderedLeft[i]>orderedRight[j]:
                combinedList.append(orderedRight[j])
                j+=1
        return combinedList
    elif len(aList)==1:
        return aList
    elif len(aList)==2:
        comparedList=compareNum(aList)
        return comparedList
    else:
        print("It's a freaking empty list")



def compareNum(twoList):
    if twoList[0]>twoList[1]:
        a=twoList[0]
        twoList[0]=twoList[1]
        twoList[1]=a
    #print("just compared two numbers", twoList[0],twoList[1])
    return twoList
print("after mergesort, the list [90,17,8,7,4,3,8,92,15,23] is",mergesort([90,17,8,7,4,3,8,92,15,23]))