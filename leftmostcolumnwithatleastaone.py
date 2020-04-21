class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        #nlogn solution
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
            