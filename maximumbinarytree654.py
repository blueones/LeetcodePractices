# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        #first intuition answer
        #not great. Since for everytime we look for the index for node, we are doing a sort.
        self.nums = nums
        def maxIndex(l,r):
            maxN = float("-inf")
            maxF = l
            for i in range(l,r):
                if self.nums[i]> maxN:
                    maxN = self.nums[i]
                    maxF = i
            return maxF
        def construct(l,r):
            if l>= r:
                return None
            indexM = maxIndex(l,r)
            node = TreeNode(self.nums[indexM])
            node.left = construct(l,indexM)
            node.right = construct(indexM+1,r)
            return node
        return construct(0, len(nums))

        


class Solution1:
    def constructMaximumBinaryTree(self,nums):
        # great solution but not intuitive
        # use iterative solution
        stackList = []
        for i in nums:
            currentNode = TreeNode(i)
            while stackList and stackList[-1] < i:
                last = stackList.pop(-1)
            if stackList:
                stackList[-1].right = currentNode
            if last:
                currentNode.left = last
            stackList.append(currentNode)
            last = None
        return stackList[0]
class Solution2:
    def constructMaximumBinaryTree(self,nums):
        #much more intuitive. to insert new item into appropriate place
        if nums == []:
            return None
        def insert(root, newitem):
            # root right now is the currently largest number. if newitem > root.val. new item becomes the new root
            newRoot = TreeNode(newitem)
            if newitem > root.val:
                newRoot.left = root
                return newRoot
            #if newitem < root.val. then put it to the right of the smallest item that's larger than newitem.
            pre = root
            seeker = root.right
            while seeker and seeker.val> newitem:
                pre = seeker
                seeker = seeker.right
            pre.right = newRoot
            newRoot.left = seeker
            return root    
            
        currentNode = TreeNode(nums[0])
        for i in range(1, len(nums),1):
            currentNode = insert(currentNode, nums[i])
        return currentNode
        
                

                


Solution().constructMaximumBinaryTree([3,2,1,6,0,5])