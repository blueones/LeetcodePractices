class Solution:
    def findKthLargest(self, nums, k):
        # quickfind solution, log(n) solution, takes O(n) memory
        # quicksort idea. a flag, a traverse and a partition.
        # when partition is k-1 then return that partition.
        self.nums = nums 
        random.shuffle(self.nums)
        self.lenN = len(nums)
        self.target = k-1
        def divide(l,r):
            flag = self.nums[r]
            #print("flag is ",flag)
            partition = l
            for traverse in range(l,r,1):
                if self.nums[traverse] > flag:
                    self.nums[partition],self.nums[traverse]=self.nums[traverse],self.nums[partition]
                    partition+=1
            self.nums[partition],self.nums[r]=self.nums[r],self.nums[partition]
            #print("list is ",self.nums," and partition is ",partition)
            return partition

        def find(l,r):
            if l == r:
                return self.nums[l]
            partition = divide(l,r)
            #print("what happened before here")
            if partition == self.target:
                #print("should've ended right here")
                return self.nums[partition]
            elif partition > self.target:
                return find(l , partition-1)
            else:
                return find(partition+1, r)

     
        return find(0,self.lenN-1)

print(Solution().findKthLargest([3,2,1,5,6,4],2))


             