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
#what if we want all of the courses.
