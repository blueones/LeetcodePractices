class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # rooms is an adjacency list already in the form of list
        #whenever enter a room, we deduct one from unvisitedroom which starts as the number of rooms
        unvisited_rooms = len(rooms)
        visited_record = [False]*unvisited_rooms
        def dfsHelper(node,visited_record,unvisited_rooms):
            if visited_record[node]:
                return unvisited_rooms
            visited_record[node] = True
            unvisited_rooms-=1
            for key in rooms[node]:
                unvisited_rooms=dfsHelper(key,visited_record,unvisited_rooms)
            return unvisited_rooms
        return True if dfsHelper(0,visited_record,unvisited_rooms)==0 else False