#to be a binary tree.
# connectivity(all nodes are connected)
# no cycle
# verges number is N-1 
# indegree and outdegree. 
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0 for i in range(n)]
        outdegree = [0 for i in range(n)]
        verge = 0
        for index in range(n):
            left_node = leftChild[index]
            right_node = rightChild[index]
            if left_node != -1:
                indegree[left_node] += 1
                outdegree[index] += 1
                verge += 1
            if right_node != -1:
                indegree[right_node] += 1
                outdegree[index] += 1
                verge += 1
        
        count_root = 0
        wrong = 0
        for index in range(n):
            if indegree[index] == 0 and outdegree[index] != 0:
                count_root += 1
            elif indegree[index] != 1 and indegree[index]!= 0:
                wrong += 1
        return (n == 1 and count_root == 0) or (count_root == 1 and  verge == n-1 and wrong == 0)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0 for i in range(n)]
        verge = 0
        for index in range(n):
            left_node = leftChild[index]
            right_node = rightChild[index]
            if left_node != -1:
                indegree[left_node] += 1
                verge += 1
            if right_node != -1:
                indegree[right_node] += 1
                verge += 1
        
        count_root = 0
        wrong = 0
        for index in range(n):
            if indegree[index] == 0:
                count_root += 1
                root = index
            elif indegree[index] != 1 and indegree[index]!= 0:
                wrong += 1
                
        if count_root != 1 or wrong != 0 or verge != n-1:
            return False
        visited = [False for i in range(n)]
        def dfs(node):
            if node == None:
                return True, 0
            if visited[node] == True:
                return False, 0
            visited[node] = True
            nodes = 1
            if leftChild[node] != -1:
                goodTree, left_nodes = dfs(leftChild[node])
                if goodTree == False:
                    return False, 0
                nodes += left_nodes
                
            if rightChild[node] != -1:
                goodTree, right_nodes = dfs(rightChild[node]) 
                if goodTree == False:
                    return False, 0
                nodes += right_nodes
            return True, nodes
        goodTree, nodes = dfs(root)
        if goodTree == True and nodes == n:
            return True
        return False              
                