class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # rooms is an adjacency list already in the form of list
        #whenever enter a room, we deduct one from unvisitedroom which starts as the number of rooms
        unvisited_count = len(rooms)
        visited_record = [False]*unvisited_count
        def dfsHelper(node,visited_record,unvisited_count):
            if visited_record[node]:
                return unvisited_count
            visited_record[node] = True
            unvisited_count-=1
            for key in rooms[node]:
                unvisited_count=dfsHelper(key,visited_record,unvisited_count)
            return unvisited_count
        return True if dfsHelper(0,visited_record,unvisited_count)==0 else False
class Solution1:
    def canVisitAllRooms(self,rooms):
        visited_record = [False]*len(rooms)
        def dfsHelper(node,visited_record):
            if visited_record[node]:
                return 
            visited_record[node] = True
            for key in rooms[node]:
                dfsHelper(key,visited_record)
        dfsHelper(0,visited_record)
        return all(visited_record)
class Solution2:
    def canVisitAllRooms(self,rooms):
        self.visited_record = [False]*len(rooms)
        self.dfsHelper(0,rooms)
        return True if all(self.visited_record) else False
    def dfsHelper(self,node,rooms):
        if self.visited_record[node]:
            return 
        self.visited_record[node] = True
        for key in rooms[node]:
            self.dfsHelper(key,rooms)
        