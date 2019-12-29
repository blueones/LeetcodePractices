# divide-and-conquer algorithm works by recursively 
# breaking down a problem into two or more sub-problems 
# of the same or related type, until these become simple 
# enough to be solved directly.


#Find count of 1 in sorted binary array
# [0,0,0,1,1]
import math
def count_binary(arrayB):
    if arrayB[0]==1:
        return len(arrayB)
    if arrayB[-1]==0:
        return 0

    
    elif arrayB[-1]==1 and arrayB[0]==0:
        print("太多数啦数不过来，divide and conquer")
        arrayF=arrayB[:math.floor(len(arrayB)/2)].copy()
        arrayL=arrayB[math.floor(len(arrayB)/2):].copy()
        if arrayF[-1]==0:
            return count_binary(arrayL)
        elif arrayF[-1]==1:
            return count_binary(arrayF)
    


def sunny_max(inputArray):
    if len(inputArray)<=2:
        if inputArray[0]>inputArray[1]:
            return inputArray[0]
        elif inputArray[0]<=inputArray[1]:
            return inputArray[1]
    else:
        print("不会做，老公欺负我")
        arrayF=inputArray[:math.floor(len(inputArray)/2)].copy()
        arrayL=inputArray[math.floor(len(inputArray)/2):].copy()
        return max(sunny_max(arrayF),sunny_max(arrayL))

print(count_binary([0,0,0,1,1,1,1]))