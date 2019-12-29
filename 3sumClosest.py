class Solution:
	def threeSum(self, nums,target):
		res = []
		nums.sort()
		print("nums is",nums)
		l = len(nums)
		for i in range(l):
			spot = nums[i]
			if i>=1 and nums[i]==nums[i-1]:
				continue
			start = i + 1
			end = l - 1

			while start<end:
				if nums[start] + nums[end] + spot == target:
					ans = nums[start]+nums[end]+spot
					return ans
					res.append(ans)
					while start<end and nums[start]==nums[start+1]:
						start+=1
					start+=1
					while start<end and nums[end]==nums[end-1]:
						end-=1
					end-=1
				elif nums[start] + nums[end] + spot>target:
					total=nums[start]+nums[end]+spot
					res.append(total)
					end-=1
				elif nums[start] + nums[end] + spot < target:
					total=nums[start]+nums[end]+spot
					res.append(total)
					start+=1
				else:
					print("What just happened?!")
		
		resultDic=dict()
		for i in res:
			resultDic[i]=abs(i-target)
	
		
		return min(resultDic,key=lambda x:resultDic.get(x))



print (Solution().threeSum([-1, 2, 1, -4],1))