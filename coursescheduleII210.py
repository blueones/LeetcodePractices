from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for i in range(numCourses)]
        dict_graph = defaultdict(set)
        verges = 0
        course_path = deque()
        for pre in prerequisites:
            dict_graph[pre[1]].add(pre[0])
            indegrees[pre[0]] += 1
            verges += 1
        stack = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                stack.append(i)
        while stack:
            current_course = stack.pop()
            course_path.append(current_course)
            for after in dict_graph[current_course]:
                indegrees[after] -= 1
                verges -= 1
                if indegrees[after] == 0:
                    stack.append(after)
        if verges != 0:
            return []
        return course_path
from collections import defaultdict
class Solution1:
    #DFS Solution. pay attention to proof of correctness. 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for i in range(numCourses)]
        dict_graph = defaultdict(set)
        verges = 0
        course_path = deque()
        visited = [False for i in range(numCourses)]
        for pre in prerequisites:
            dict_graph[pre[1]].add(pre[0])
            indegrees[pre[0]] += 1
            verges += 1
        stack = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                stack.append(i)
        while stack:
            current_course = stack.pop()
            for after in dict_graph[current_course]:
                indegrees[after] -= 1
                verges -= 1
                if indegrees[after] == 0:
                    stack.append(after)
        #check if it's a directed acyclic graph
        if verges != 0:
            return []
        def dfs(node):
            for after in dict_graph[node]:
                if visited[after] == False:
                    visited[after] = True
                    dfs(after)
            course_path.append(node)
        for i in range(numCourses):
            if visited[i] == False:
                visited[i] = True
                dfs(i)
        ans = []
        while course_path:
            ans.append(course_path.pop())
        return ans
        
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
     #use two flags to mark if a node is visited. and if a node is on the path. for the path, use backtracking technique to unmark when retrieve from a path.
        dict_graph = defaultdict(set)
    
        course_path = deque()
        visited = [False for i in range(numCourses)]
        path = [False for i in range(numCourses)]
        for pre in prerequisites:
            dict_graph[pre[1]].add(pre[0])
        self.cycle = False    
        
        def dfs(node):
            
            for after in dict_graph[node]:
                if path[after] == True:
                    self.cycle = True
                    return
                if visited[after] == False:
                    visited[after] = True
                    path[after] = True
                    dfs(after)
                    path[after] = False
            course_path.append(node)
        for i in range(numCourses):
            if visited[i] == False:
                visited[i] = True
                path[i] = True
                dfs(i)
                path[i] = False
                
        if self.cycle == True:
            return []
        ans = []
        while course_path:
            ans.append(course_path.pop())
        return ans
        
       