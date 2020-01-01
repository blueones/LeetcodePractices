# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root) :
        #use recursion to calculate
        self.maxN=0
        def dfs(root,parent):
            if root==None:
                if self.maxN<1:
                        self.maxN=1
                return 1
            if root!=None:
                if root.val==parent+1:
                    num=max(dfs(root.left,root.val),dfs(root.right,root.val))
                    if self.maxN<num+1:
                        self.maxN=num+1
                    return num+1
                else:
                    num=max(dfs(root.left,root.val),dfs(root.right,root.val))
                    return 1
        if root==None:
            return 0
        dfs(root,root.val)
        return self.maxN

class Solution2:
    def longestConsecutive(self, root: TreeNode) -> int:
        #previous is the parent of the current root
        #counter keeps track of consecutive values before root
        #ret is an array of one element, used to store the result
        def dfs(root, ret, previous=None, counter=0):
            if not root:
                #we are at the leaf node, check if counter has larger value
                ret[0] = max(ret[0], counter)
                return
            if previous and previous.val + 1 == root.val:
                #if previous value is less than current by 1, counter increments
                dfs(root.left, ret, root, counter + 1)
                dfs(root.right, ret, root, counter + 1)
            else:
                #we are either at start, or the previous value is not less than current by 1
                #first update the return value because we are breaking previous consecutive counts
                ret[0] = max(ret[0], counter)
                dfs(root.left, ret, root, 1)
                dfs(root.right, ret, root, 1)
        ret = [0]
        dfs(root, ret)
        return ret[0]       

            
SunnyNode=TreeNode(1)
SunnyNode.right=TreeNode(3)
SunnyNode.right.left=TreeNode(2)
SunnyNode.right.right=TreeNode(4)
SunnyNode.right.right.right=TreeNode(5)

print(Solution().longestConsecutive(SunnyNode))