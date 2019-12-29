class Solution:
	def threeSum(self, nums):
		res = []
		nums.sort()
		l = len(nums)
		for i in range(l):
			target = nums[i]
			if i>=1 and nums[i]==nums[i-1]:
				continue
			if target>0:
				break
			start = i + 1
			end = l - 1
			while start<end:
				if nums[start] + nums[end] + target ==0:
					ans = [target,nums[start],nums[end]]
					res.append(ans)
					while start<end and nums[start]==nums[start+1]:
						start+=1
					start+=1
					while start<end and nums[end]==nums[end-1]:
						end-=1
					end-=1
				elif nums[start] + nums[end] + target > 0:
					end-=1
				elif nums[start] + nums[end] + target < 0:
					start+=1
				else:
					print("What just happened?!")
		return res

        # i=0
        # j=len(nums)-1
        # resultL=list()
        # dictionaryT=dict()
        # for y in range(len(nums)):
        #     dictionaryT[nums[y]]=y

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         print("i is",i,"j is",j)
        #         targetN=0-nums[i]-nums[j]
        #         if targetN in dictionaryT:
        #             if i==dictionaryT[targetN] or j==dictionaryT[targetN]:
        #                 continue
        #             listS=[nums[i],nums[j],targetN]
        #             listS.sort()
        #             if listS not in resultL:
        #                 resultL.append(listS)
        # return resultL
print(Solution().threeSum([-1,0,1,2,-1,-4]))