def maximumArraySub(aList):
    #input: an array
    #output:maximum sum of a subarray in this array
    #algorithm:
    if len(aList)==0:
        return "the list is freaking empty"
    elif len(aList)==1:
        return aList[0]
    elif len(aList)>=2:
        currentSum=0
        counter=list()
        for a in range(len(aList)):
            currentSum+=aList[a]
            if currentSum<=0:
                currentSum=0
            counter.append(currentSum)
        return max(counter)


        

