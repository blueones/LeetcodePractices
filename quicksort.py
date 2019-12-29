import random

class Quicksort:
    def __init__(self,listtosort):
        self.list=listtosort
        self.listLen=len(listtosort)
    def quicksort(self):
        if self.listLen==0:
            return []
        #shuffle the list
        random.shuffle(self.list)
        #start sorting the list
        self.sort(self.list,0,self.listLen-1)
        return self.list
    def sort(self,listS,beginS,endS):
        if beginS<endS:
            partitionIndex=self.partition(listS,beginS,endS)
            print(listS)
            self.sort(listS,beginS,partitionIndex-1)
            self.sort(listS,partitionIndex+1,endS)
        #sorting the list involves step1, partition
        #then sort the finished product on the left and on the right, RECURSIVELY
    def partition(self,listP,beginL,endL):
        partitionB=beginL
        partitionN=listP[beginL]
        leftF=beginL
        rightF=endL
        while leftF<rightF:
            while listP[leftF]<=partitionN:
                if leftF==endL:
                    break
                leftF+=1
            while listP[rightF]>partitionN:
                if rightF==beginL:
                    break
                rightF-=1
            if leftF>=rightF:
                break
            listP[leftF],listP[rightF]=listP[rightF],listP[leftF]
        listP[rightF],listP[partitionB]=listP[partitionB],listP[rightF]
        return rightF

        #get a list, use the first of the list as the partition barrier
        
        #mark the beginning of the list as i and mark the end of the list as j
        #increment i and j, then compare list[i] and list[j], if list[i]>=list[0](the partition barrier right now), and if list[j]< list[0]
        # then the invariant that all elements on the left of i are less than the partition barrier and all elements on the right of j are bigger than the partition barrier
        # replace i and j, keep going until i>j
        #replace j with list[0](the partition barrier), 
        #now from the begining of the list to the parition barrier are a list that have all elements smaller than from the partition barrier to the end of the list.
        


list1=[2,43,1,67,65,58,3,2,9,7,7,7,10]
print(Quicksort(list1).quicksort())