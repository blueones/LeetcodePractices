class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        frequencyDict = {}
        for item in arr1:
            frequencyDict[item]=1
        for item2 in arr2:
            if item2 in frequencyDict:
                frequencyDict[item2]+=1
        for item3 in arr3:
            if item3 in frequencyDict:
                frequencyDict[item3]+=1
        resultL = []
        for item in frequencyDict:
            if frequencyDict[item]==3:
                resultL.append(item)
        return resultL
class Solution1:
    def arraysIntersection(self,arr1,arr2,arr3):
        index1 = index2 = index3=0
        result = []
        len1 = len(arr1)
        len2 = len(arr2)
        len3 = len(arr3)
        while index1<len1 and index2< len2 and index3<len3:
            if arr1[index1]==arr2[index2]==arr3[index3]:
                result.append(arr1[index1])
                index1+=1
                index2+=1
                index3+=1
            else:
                maxCurrent = max(arr1[index1],arr2[index2],arr3[index3])
                if arr1[index1]<maxCurrent:
                    index1+=1
                if arr2[index2]<maxCurrent:
                    index2+=1
                if arr3[index3]<maxCurrent:
                    index3+=1
        return result
            

            