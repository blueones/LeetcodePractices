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
        
class Solution2:
    def kClosest(self, points, K):
        #quickfind
        def quick_find(start, end):
            end_pivot = points[end]
            pivot_distance = end_pivot[0]**2+end_pivot[1]**2
            pivot = start
            for i in range(start, end, 1):
                if points[i][0]**2+points[i][1]**2 <= pivot_distance:
                    points[pivot], points[i] = points[i], points[pivot]
                    pivot += 1
            points[pivot], points[end] = points[end], points[pivot]
            return pivot
                    
                    
        def findKth(start, end):
            pivot = quick_find(start, end)
            if pivot == K - 1:
                print(pivot)
                return pivot
            elif pivot < K-1:
                return findKth(pivot+1, end)
            else:
                return findKth(start, pivot-1)
        pivot = findKth(0, len(points)-1)
        ans = points[:pivot+1]
        return ans