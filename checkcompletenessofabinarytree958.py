# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # mark each node with a counter. at the end, if it's complete, the counter should match with the length of the Tree.
        if root == None:
            return True
        dictN = {root:1}
        listN = [1]
        queueL = [root]
        while queueL:
            currentN = queueL.pop(0)
            v = dictN[currentN]
            if currentN.left:
                leftV = 2*v
                listN.append(leftV)
                dictN[currentN.left]= leftV
            if currentN.right:
                rightV = 2*v+1
                listN.append(rightV)
                dictN[currentN.right]= rightV
        import pdb; pdb.set_trace()
        return len(listN) == listN[-1]
sunnyNode = TreeNode(1)
sunnyNode.left = TreeNode(2)
sunnyNode.right = TreeNode(3)
sunnyNode.left.left = TreeNode(4)
sunnyNode.left.right = TreeNode(5)
sunnyNode.right.right = TreeNode(7)
Solution().isCompleteTree(sunnyNode)