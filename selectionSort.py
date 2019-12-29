class SelectionSort:
    def selectionSort(self,listS):
        leng=len(listS)
        for i in range(0,leng,1):
            currentmin=i
            for j in range(i+1,leng,1):
                if listS[currentmin]>listS[j]:
                    currentmin=j
            listS[i],listS[currentmin]=listS[currentmin],listS[i]
        return listS


print(SelectionSort().selectionSort([3,2,5,13,27,21,20,4]))
