# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(node1,node2):
            '''create a new tree'''
            if node1 and node2:
                nodeC = TreeNode(node1.val+node2.val)
                nodeC.left = dfs(node1.left,node2.left)
                nodeC.right = dfs(node1.right,node2.right)
            elif node1:
                nodeC = TreeNode(node1.val)
                nodeC.left = dfs(node1.left,None)
                nodeC.right = dfs(node1.right,None)
            elif node2:
                nodeC = TreeNode(node2.val)
                nodeC.left = dfs(None,node2.left)
                nodeC.right = dfs(None,node2.right)
            else:
                return None
            return nodeC

        return dfs(t1,t2)
            
class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''create a new tree'''
        '''modified solution, does not create new nodes. but to modify the existing tree's nodes'''
        if t1 and t2:
            t1.val+=t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
            return t1
        elif t1:
            return t1
        elif t2:
            return t2
        else:
            return None
class Solution3:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''iterative way to do this one'''
        '''return t1'''
        '''change what it is in t1'''
        '''t1 is the focus'''
        if t1 == None:
            return t2
        stackN = [(t1,t2)]
        while stackN != []:
            node1, node2=stackN.pop(-1)
            if node1 == None and node2 == None:
                continue
            elif node1 and node2:
                node1.val += node2.val
                if node1.left == None:
                    node1.left = node2.left
                else:
                    stackN.append((node1.left,node2.left))
                if node1.right == None:
                    node1.right = node2.right
                else:
                    stackN.append((node1.right,node2.right))
            '''when node2 is None, there is no handling needed, 
            since we are returning t1 in the end, so there is really no need to append.
            since it will just stay the same as what it currently is for t1'''    
            # elif node1:
            #     stackN.append((node1.left, None))
            #     stackN.append((node1.right, None))
            '''we wont have node1 is None and node2 is not None since in line60,61 and line64,65, we copy node2 over to be in t1. important.'''
            # elif node2:
            #     stackN.append((None,node2.left))
            #     stackN.append((None, node2.right))
        return t1


Tree1=TreeNode(1)
Tree1.left=TreeNode(3)
Tree1.right=TreeNode(2)
Tree1.left.left=TreeNode(5)
Tree2=TreeNode(2)
Tree2.left=TreeNode(1)
Tree2.right=TreeNode(3)
Tree2.left.right=TreeNode(4)
Tree2.right.right=TreeNode(7)
print(Solution3().mergeTrees(Tree1,Tree2))