class NumArray:

    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.matrix = [[""for i in range(self.length)] for i in range(self.length)]
        for i in range(self.length):
            self.matrix[i][i]=nums[i]
        for i in range(self.length):
            for j in range(i+1,self.length):
                self.matrix[i][j]=self.matrix[i][j-1]+self.matrix[j][j]
                
        
                    
        

    def sumRange(self, i: int, j: int) -> int:
        return self.matrix[i][j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)