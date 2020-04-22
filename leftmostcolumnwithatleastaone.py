# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        #nlogn solution, binary search
        row, column = binaryMatrix.dimensions()
        
        def helper(checked_column):
            for i in range(0,row):
                if binaryMatrix.get(i,checked_column) == 1:
                    return True
            return False
        
        
        start = 0
        end = column
        while start < end:
            mid = (start+end)//2
            if helper(mid):
                end = mid
            else:
                start = mid+1
                
        return start if start < column else -1

class Solution1:
    def leftMostColumnWithOne(self,binaryMatrix):
         #use a pointer 
         # O(n+m)
        row, column = binaryMatrix.dimensions()
        pointer_row = 0
        pointer_column = column
        while pointer_row < row or pointer_column > 0:
            if binaryMatrix.get(pointer_row, pointer_column-1) == 1:
                if pointer_column-1 == 0:
                    return 0
                else:
                    pointer_column -= 1
            else:
                if pointer_row == row-1:
                    break
                else:
                    pointer_row += 1
        return pointer_column if pointer_column != column else -1
