class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code
        self.max_res = 0
        self.memo = [[None for i in range(m+1)] for j in range(len(A))]
        def dfs(index, current_storage):
            if self.memo[index][current_storage]:
                return self.memo[index][current_storage]
            if current_storage == 0:
                self.memo[index][current_storage] = 0
                return 0
            
            if index == len(A) - 1:
                if current_storage >= A[index]:
                    self.memo[index][current_storage] = A[index]
                    return A[index]
                else:
                    self.memo[index][current_storage] = 0
                    return 0
            else:
                max_rest = 0

                include_rest = 0
                if current_storage - A[index] >= 0:
                    include_rest = dfs(index+1, current_storage - A[index]) + A[index]
                not_rest = dfs(index+1, current_storage)
                max_rest = max(include_rest, not_rest)
                
                self.memo[index][current_storage] = max_rest
                self.max_res = max(self.max_res,  max_rest)
                return max_rest
                    
        dfs(0, m)
        
        return self.max_res
