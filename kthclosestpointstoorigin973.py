class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        list_all = []
        for index in range(len(points)):
            point = points[index]
            list_all.append((point[0]**2+point[1]**2, index))
        list_all.sort(key = lambda x:x[0])
        ans = []
        for value, index in list_all[:K]:
            print(index)
            ans.append(points[index])
        return ans

class Solution1:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x:x[0]**2+x[1]**2)
        return points[:K]
        