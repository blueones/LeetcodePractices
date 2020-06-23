class Solution:
    def canFinish(self, numCourses, prerequisites):
        #go thru list of edges create Graph with the representation of list of adjacency nodes.
        #mark the ones that has been chosen in a graph
        #check cycle in this graph. using DFS. when checking cycle, make sure on each path you are not revisiting nodes that you've been.
        #  if find node that has been visited in a path, then found cycle.
        #final result is a boolean. 
        self.courses=Graph(numCourses)
        self.visited={node:False for node in range(numCourses)}
        self.browsed={node:False for node in range(numCourses)}
        for relation in prerequisites:
            self.courses.addEdge(relation[0],relation[1])
        print(self.courses.adj)
        
        for course in self.courses.adj:
            if self.browsed[course]==False:
                self.browsed[course]=True
                if self.visit(course)==False:
                    return False
        return True

    def visit(self,course):
        self.visited[course]=True
        for aftercourse in self.courses.adj[course]:
            if self.visited[aftercourse]==True:
                return False
            elif self.visited[aftercourse]==False:
                if self.visit(aftercourse)==False:
                    return False
        self.visited[course]=False
        return True

class Graph:
    def __init__(self,nodes):
        self.Vnum=nodes
        self.adj={node:[] for node in range(nodes)}
    def addEdge(self,course, prere):
        self.adj[prere].append(course)

graph_edge = [[0,1],[3,1],[1,3],[3,2]]
    


            




print(Solution().canFinish(4,graph_edge))

            
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict_courses = defaultdict(list)
        for prerequisite in prerequisites:
            dict_courses[prerequisite[0]].append(prerequisite[1]) 
        def dfs(node, path):
            if path[node] == True:
                return False
            else:
                visited[node] = True
                path[node] = True
                for neighbor in dict_courses[node]:
                    if dfs(neighbor, path) == False:
                        return False
                path[node] = False
                return True

        visited = [False for i in range(numCourses)]
        path = [False for i in range(numCourses)]
        
        for i in range(numCourses):
            if visited[i] == False:
                if dfs(i, path) == False:
                    return False
                visited[i] = True
        return True
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort
        indegree = [0 for i in range(numCourses)]
        verges = 0
        dict_graph = defaultdict(set)
        for pre in prerequisites:
            indegree[pre[0]] += 1
            dict_graph[pre[1]].add(pre[0])
            verges += 1
        
        stack = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        
        while stack:
            current_node = stack.pop()
            for after_course in dict_graph[current_node]:
                indegree[after_course] -= 1
                verges -= 1
                if indegree[after_course] == 0:
                    stack.append(after_course)
        if verges != 0:
            return False
        return True
        