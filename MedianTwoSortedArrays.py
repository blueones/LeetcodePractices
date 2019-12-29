import math
class Solution:

    def findKthElement(self,nums1,m,nums2,n,k):
        print(nums1,nums2,m,n,k)
        median1=math.floor((m+1)/2)
        median2=math.floor((n+1)/2)
        medianAll=math.floor((m+n+1)/2)
       # print(median1,median2,medianAll)
        if m<=2 or n<=2:
            return sorted(nums2+nums1)[k-1]
        if k==m+n:
            return max(nums1[-1],nums2[-1])
        if m==0:
            return nums2[k-1]

        if n==0:
            return nums1[k-1]

        elif k<m+n:

            # print("hi")
        # if m>=1 and n>=1:
            if k>=medianAll:
                if nums1[median1-1]>=nums2[median2-1]:
                    print(1)
                    return self.findKthElement(nums1,m,nums2[median2-1:],n-median2+1,k-median2+1)
                elif nums2[median2-1]>nums1[median1-1]:
                    print(2)
                    return self.findKthElement(nums1[median1-1:],m-median1+1,nums2,n,k-median1+1)
            elif k<medianAll:
                if nums1[median1-1]>=nums2[median2-1]:
                    print(3)
                    return self.findKthElement(nums1[:median1],m-median1,nums2[:],n,k)
                elif nums2[median2-1]>nums1[median1-1]:
                    print(4)
                    return self.findKthElement(nums1[:],m,nums2[:median2],n-median2,k)
        

    def findMedianSortedArrays(self,nums1,nums2):
        m=len(nums1)
        n=len(nums2)
        if (m+n)%2==0:
            k=int((m+n)/2)
            vk=self.findKthElement(nums1,m,nums2,n,k)
            vk1=self.findKthElement(nums1,m,nums2,n,k+1)
            return (vk+vk1)/2
        elif (m+n)%2==1:
            k=int((m+n+1)/2)
            vk=self.findKthElement(nums1,m,nums2,n,k)
            return vk


print(Solution().findKthElement([1,2],2,[3,4],2,2))
