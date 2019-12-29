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

            
