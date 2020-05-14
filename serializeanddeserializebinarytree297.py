# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
#Stack. BFS way.
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []
        queue = deque()
        queue.append(root)
        seri_list = [root.val]
        while queue:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
                seri_list.append(current.left.val)
            else:
                seri_list.append(None)
            if current.right:
                queue.append(current.right)
                seri_list.append(current.right.val)
            else:
                seri_list.append(None)
        print(seri_list)
        return seri_list
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == []:
            return None
        
        nodes_deque = deque()
        root = TreeNode(data[0])
        nodes_deque.append(root)
        index_list = 0
        while nodes_deque and index_list < len(data):
            current_node = nodes_deque.popleft()
            if current_node != None:
                index_list += 1
                if index_list < len(data):
                    current_node_left = TreeNode(data[index_list]) if data[index_list] != None else None
                    current_node.left = current_node_left
                else:
                    continue

                index_list += 1
                if index_list < len(data):
                    current_node_right = TreeNode(data[index_list]) if data[index_list] != None else None
                    current_node.right = current_node_right
                else:
                    continue
                nodes_deque.append(current_node_left)
                nodes_deque.append(current_node_right)
        return root
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if data == []:
    #         return None
        
    #     nodes_deque = deque()
    #     root = TreeNode(data[0])
    #     nodes_deque.append(root)
    #     index_list = 0
    #     while nodes_deque and index_list < len(data):
    #         current_node = nodes_deque.popleft()
    #         if current_node != None:
    #             index_list += 1
    #             if index_list < len(data):
    #                 current_node_left = TreeNode(data[index_list]) if data[index_list] != None else None
    #                 current_node.left = current_node_left
    #                 nodes_deque.append(current_node_left)
                

    #             index_list += 1
    #             if index_list < len(data):
    #                 current_node_right = TreeNode(data[index_list]) if data[index_list] != None else None
    #                 current_node.right = current_node_right
    #                 nodes_deque.append(current_node_right)
                
                
                
    #     return root
        
class Solution1:
    #DFS solution. preorder traversal. serialize and deserialize.