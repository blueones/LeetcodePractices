# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        return self.sumP(root,0,sum,[])
    def sumP(self,root,CurrentS,sum,listN):
        if root==None:
            CurrentS=0
            return []
        if root!=None:
            listC=[root.val]
            CurrentS+=root.val
            listN+=listC
            listS=list()
            if root.left==None and root.right==None:
                if CurrentS==sum:
                    listS.append(listN)
            leftN=root.left
            listNleft=listN.copy()
            rightN=root.right
            listNright=listN.copy()
            leftsumP=list()
            rightsumP=list()
            if leftN:
                leftsumP=self.sumP(leftN,CurrentS,sum,listNleft)
            if rightN:
                rightsumP=self.sumP(rightN,CurrentS,sum,listNright)
            return listS+leftsumP+rightsumP

class Solution2:
    def pathSum(root,sum):
        #recursive Jan 25th
        if root == None:
            return []
        self.dictNode = {root: None}
        self.leafs = []
        def dfs(node, currentSum):
            if node.left == None and node.right == None:
                if currentSum == sum:
                    self.leafs.append(node)
            if node.left:
                self.dictNode[node.left] = node
                dfs(node.left, currentSum+node.left.val)
            if node.right:
                self.dictNode[node.right] = node
                dfs(node.right,currentSum+node.right.val)
        dfs(root, root.val)
        resultList = []
        if self.leafs == []:
            return []
        for leaf in self.leafs:
            leafpath = []
            while leaf != None:
                leafpath.append(leaf.val)
                leaf = self.dictNode[leaf]
            resultList.append(leafpath[::-1]) #make sure to reverse the list. since it's leaf to root
        return resultList

class Solution2deduct:
    def pathSum(root,sum):
        #recursive Jan 25th, use deduct current node value from sum instead of adding. 
        if root == None:
            return []
        self.dictNode = {root: None}
        self.leafs = []
        def dfs(node, currentSum):
            if node.left == None and node.right == None:
                if currentSum == 0:
                    self.leafs.append(node)
            if node.left:
                self.dictNode[node.left] = node
                dfs(node.left, currentSum-node.left.val)
            if node.right:
                self.dictNode[node.right] = node
                dfs(node.right,currentSum-node.right.val)
        dfs(root, sum - root.val)
        resultList = []
        if self.leafs == []:
            return []
        for leaf in self.leafs:
            leafpath = []
            while leaf != None:
                leafpath.append(leaf.val)
                leaf = self.dictNode[leaf]
            resultList.append(leafpath[::-1]) #make sure to reverse the list. since it's leaf to root
        return resultList







class Solution3:
    def pathSum(root,sum):
        #iterative
        if root == None:
            return []
        stackList = [(root, sum - root.val)]
        self.leafs = []
        self.dictNodes = {root: None}
        self.resultpath = []
        while stackList != []:
            currentNode, currentSum = stackList.pop(-1)
            if currentNode.left == None and currentNode.right == None:
                if currentSum == 0:
                    self.leafs.append(currentNode)
            if currentNode.left:
                stackList.append((currentNode.left,currentSum - currentNode.left.val))
                self.dictNodes[currentNode.left]=currentNode
            if currentNode.right:
                stackList.append((currentNode.right, currentSum - currentNode.right.val))
                self.dictNodes[currentNode.right] = currentNode
        if self.leafs == []:
            return []
        for leaf in self.leafs:
            path = []
            while leaf != None:
                path.append(leaf.val)
                leaf = self.dictNodes[leaf]
            self.resultpath.append(path[::-1])
        return self.resultpath
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution4:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        def helper(node, carry, path):
            if node!= None:
                path.append(node.val)
                if node.left == None and node.right == None:
                    if carry+node.val == sum:
                        self.ans.append(path.copy())
                else:

                        helper(node.left, carry+node.val, path)
                        helper(node.right, carry+node.val, path)
                path.pop(-1)
        helper(root, 0, [])
        return self.ans
        
            
            