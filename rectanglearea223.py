class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        #on x axis: A, C,      E,G
        #on Y axis: B, D       F,H
        # result area will be  area1 + area2 - overlapping
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        def helper(point1, point2, point3, point4):
            #return overlapping
            # point1 < point3
                # point2 < point3
                # point2 > point3
                    #point 2< point4
                    #point2 > point4
            # point1 > point3
            if point1 >= point3:
                point1, point2, point3, point4 = point3, point4, point1, point2
                
            if point2 < point3:
                return 0
            else:
                if point2< point4:
                    return point2 - point3
                else:
                    return point4 - point3
        overlapping_row = helper(A, C, E, G)
        overlapping_column = helper(B, D, F, H)
        return area1+area2- overlapping_row*overlapping_column