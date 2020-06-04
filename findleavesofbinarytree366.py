# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        def getDepth(node, ans_list):
            if node == None:
                return -1
            node.depth = 1+ max(getDepth(node.left, ans_list), getDepth(node.right, ans_list))
            if len(ans_list) == node.depth:
                ans_list.append([node.val])
            else:
                ans_list[node.depth].append(node.val)
            return node.depth
        ans_list = []
        getDepth(root, ans_list)
        return ans_list
class Solution1:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        #make ans a class variable.
        ans = []
        def dfs(node):
            if node == None:
                return -1
            
            current_depth = 1 + max(dfs(node.left),dfs(node.right))
            if len(ans) == current_depth:
                ans.append([node.val])
            else:
                ans[current_depth].append(node.val)
            return current_depth
        dfs(root)
        return ans