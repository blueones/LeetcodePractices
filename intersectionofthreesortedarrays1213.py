class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        #three pointers
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
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        len1 = len(arr1)
        len2 = len(arr2)
        len3 = len(arr3)
        def helper(input_arr1, input_arr2):
            index2 = 0
            len2 = len(input_arr2)
            resultL =[]
            for item in input_arr1:
                
                while index2<len2 and input_arr2[index2]<item:
                    index2+=1
                if index2<len2 and input_arr2[index2]==item:
                    resultL.append(item)
                    index2+=1
                elif index2< len2 and input_arr2[index2]>item:
                    continue
                elif index2== len2:
                    break
            return resultL
        result12 = helper(arr1,arr2)
        return helper(result12,arr3)
        