class InsertionSort:
    def insertionSort(self,listI):
        leng=len(listI)
        for i in range(0,leng,1):
            for j in range(i,0,-1):
                if listI[j]<listI[j-1]:
                    listI[j],listI[j-1]=listI[j-1],listI[j]
                else:
                    break
        return listI
print(InsertionSort().insertionSort([3,2,5,13,27,21,20,4]))
