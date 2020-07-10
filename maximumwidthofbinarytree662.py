# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque()
        if root == None:
            return 0
        max_width = 0
        queue.append(root)
        while queue:
            number_level = len(queue)
            max_width = max(max_width, number_level)
            new_queue = deque()
            for i in range(number_level):
                current_node = queue.popleft()
                
                if current_node == None:
                    new_queue.append(None)
                    new_queue.append(None)
                else:
                    new_queue.append(current_node.left)
                    new_queue.append(current_node.right)
            while len(new_queue)!= 0 and new_queue[0] == None:
                new_queue.popleft()
            while len(new_queue)!= 0 and new_queue[-1] == None:
                new_queue.pop()
            queue = new_queue
        return max_width
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque()
        if root == None:
            return 0
        max_width = 0
        queue.append(root)
        while queue:
            number_level = len(queue)
            max_width = max(max_width, number_level)
            new_queue = deque()
            for i in range(number_level):
                current_node = queue.popleft()
                
                if current_node == None:
                    new_queue.append(None)
                    new_queue.append(None)
                else:
                    new_queue.append(current_node.left)
                    new_queue.append(current_node.right)
            while len(new_queue)!= 0 and new_queue[0] == None:
                new_queue.popleft()
            while len(new_queue)!= 0 and new_queue[-1] == None:
                new_queue.pop()
            queue = new_queue
        return max_width
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque()
        if root == None:
            return 0
        queue.append((root,0))
        max_width = 0
        while queue:
            number_level = len(queue)
            for i in range(number_level):
                
                current_node, index = queue.popleft()
                if i == 0:
                    left = index
                if i == number_level-1:
                    right = index
                if current_node.left:
                    queue.append((current_node.left, index*2))
                if current_node.right:
                    queue.append((current_node.right, index*2+1))
            max_width = max(max_width, right-left+1)
        return max_width
                                                                                                                          
            