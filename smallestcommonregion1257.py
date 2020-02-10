class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = None
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # first make this into a n-ray tree
        # find lowest common ancestor
        #probably one solution dealing with trees another solution dealing with lists themselves
        parent = {}
        for listofR in regions:
            for index in range(1,len(listofR)):
                parent[listofR[index]]= listofR[0]
        #referring to how to find the lowest common ancestor 236 using the recursive solution2.
        parent[regions[0][0]]= None
        pathregion1 = set()
        while region1:
            pathregion1.add(region1)
            region1 = parent[region1]
        while region2 not in pathregion1:
            region2 = parent[region2]
        return region2
                