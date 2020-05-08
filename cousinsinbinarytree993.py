class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #remember each nodes parent and level
        dict_nodes = {root.val:(0, None)}
        def helper(node, level):
            if node != None:
                helper(node.left, level+1)
                helper(node.right, level+1)
                if node.left:
                    dict_nodes[node.left.val] = (level+1, node.val)
                if node.right:
                    dict_nodes[node.right.val] = (level+1, node.val)
        helper(root, 0)
        x_level, x_parent = dict_nodes[x]
        y_level, y_parent = dict_nodes[y]
        if x_level == y_level and x_parent != y_parent:
            return True
        return False
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #when find either one, mark the level and for the rest only go that far down the path.
        self.recorded_depth = None
        def helper(node, level, parent, x, y):
            if node:
                if node.val == x or node.val == y:
                    if self.recorded_depth == None:
                        self.recorded_depth = (level, parent)
                    else:
                        if level == self.recorded_depth[0]:
                            if parent != self.recorded_depth[1]:
                                return True
                else:
                    if self.recorded_depth and self.recorded_depth[0] <= level:
                        return False
                    return helper(node.left, level+1, node.val, x, y) or helper(node.right, level+1, node.val, x, y)
                            
                        
            else:
                return False
                
        return helper(root, 0, None, x, y)
class Solution2:
    def isCousins(self, root, x, y):
        #bfs normally we use queue. but this question is doing level order traversal so I guess it's okay. 
        stack = [(root, None)]
        flag = False
        marked_parent = None
        while stack:
            new_layer = []
            
            while stack:
                current_node, parent = stack.pop()
                if current_node.val == x or current_node.val == y:
                    if flag == True:
                        if parent != marked_parent:
                            return True
                        else:
                            return False
                    else:
                        flag = True
                        marked_parent = parent

                if current_node.left:
                    new_layer.append((current_node.left, current_node.val))
                if current_node.right:
                    new_layer.append((current_node.right, current_node.val))
            stack = new_layer
            if flag == True:
                return False
class Solution3:
    def isCousins(self, root, x, y):
        #bfs using stack.... normally we use queue. but this question is doing level order traversal so I guess it's okay. 
        #cleaned up
        stack = [(root, None)]
        flag = False
        marked_parent = None
        while stack:
            new_layer = []
            
            while stack:
                current_node, parent = stack.pop()
                if current_node.val == x or current_node.val == y:
                    if flag == True:
                        if parent != marked_parent:
                            return True
                        return False
                    flag = True
                    marked_parent = parent

                if current_node.left:
                    new_layer.append((current_node.left, current_node.val))
                if current_node.right:
                    new_layer.append((current_node.right, current_node.val))
            stack = new_layer
            if flag == True:
                return False
from collections import deque
class Solution4:
    def isCousins(self, root, x, y):
        #BFS using queue and counter using null to mark a different parent.
        queue = deque()
        queue.append(root)
        while queue:
            length_level = len(queue)
            siblings = False
            cousins = False
            for i in range(length_level):
                current_node = queue.popleft()
                if current_node == None:
                    siblings = False
                else:
                    if current_node.val == x or current_node.val == y:
                        if siblings == False and cousins == True:
                            return True
                        siblings = True
                        cousins = True
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                    queue.append(None)
            if cousins == True:
                return False
        return False

