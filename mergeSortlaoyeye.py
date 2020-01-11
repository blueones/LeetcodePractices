class Mergesort:
    # here is how to perform a mergesort.
    # create a auxiliary list, 
    # then divide list up to two parts, then recursively sort the divided lists. 
    # merge two parts. to put into auxiliary list. 
    def __init__(self,listI):
        self.lenL=len(listI)
        self.list=listI.copy()
        self.auxL=listI.copy()
    def merge(self,startIndex, midpoint, endIndex):
        flagL=startIndex
        flagR=midpoint+1
        for copyA in range(startIndex,endIndex+1,1):
            self.auxL[copyA]=self.list[copyA]
        # print("self.auxL is ",self.auxL)
        # print("start, mid and end are ", startIndex,midpoint,endIndex)
        for flagA in range(startIndex,endIndex+1,1):
            if flagL>midpoint:
                # print("where1")
                self.list[flagA]=self.auxL[flagR]
                flagR+=1
            elif flagR>endIndex:
                # print("where2")
                self.list[flagA]=self.auxL[flagL]
                flagL+=1
            elif self.auxL[flagL]>self.auxL[flagR]:
                # print("where3")
                # print("entered here","flagl and r are ", flagL,flagR)
                self.list[flagA]=self.auxL[flagR]
                flagR+=1
            else:
                # print("where4")
                # print("entered here","flagl and r are ", flagL,flagR)
                self.list[flagA]=self.auxL[flagL]
                flagL+=1
            #print("self.auxL is now ",self.auxL)
            #print("flagA is now",self.auxL, "list[flagA] is now ",self.list[flagA])
        #print("after merge, list is now",self.list)

    def sortL(self,startIndex,endIndex):
        lengthL=endIndex-startIndex+1
        if lengthL==2:
            if self.list[startIndex]>self.list[endIndex]:
                self.list[startIndex]=self.auxL[endIndex]
                self.list[endIndex]=self.auxL[startIndex]
        elif lengthL>2:
            midPoint=startIndex+lengthL//2
            #print("now the midpoint is",midPoint)
            self.sortL(startIndex,midPoint)
            # print("entering second half with midpoint+1 being",midPoint+1,"endindex is ",endIndex)
            self.sortL(midPoint+1,endIndex)
            self.merge(startIndex,midPoint,endIndex)
        elif lengthL==1:
            #print("have we entered here?")
            # print("the one item not changed is", self.list[startIndex])
            self.list[startIndex]=self.auxL[startIndex]
        print("self.list is",self.list)
        #print("self.auxL is ",self.auxL)
    def mergesortF(self):
        if self.lenL<=1:
            return self.list
        self.sortL(0,self.lenL-1)
        return self.list


testingL=[23,24]
print(Mergesort(testingL).mergesortF())
        




        
    