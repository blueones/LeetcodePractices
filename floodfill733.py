class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        column = len(image[0])
        old_color = image[sr][sc]
        def helper(pixel_row, pixel_column):
            
            image[pixel_row][pixel_column] = newColor
            if ifValid(pixel_row+1, pixel_column) and image[pixel_row+1][ pixel_column] == old_color:
                helper(pixel_row+1, pixel_column)
            if ifValid(pixel_row-1, pixel_column) and image[pixel_row-1][ pixel_column] == old_color:
                helper(pixel_row-1, pixel_column)
            if ifValid(pixel_row, pixel_column+1) and image[pixel_row][ pixel_column+1] == old_color:
                helper(pixel_row, pixel_column+1)
            if ifValid(pixel_row, pixel_column-1) and image[pixel_row][ pixel_column-1] == old_color:
                helper(pixel_row, pixel_column-1)

        def ifValid(pixel_row, pixel_column):
            if pixel_row >= 0 and pixel_row < row and pixel_column >= 0 and pixel_column < column:
                return True
            return False
        #easy to miss this. clarifying problem.
        if old_color == newColor:
            return image
        helper(sr, sc)
        return image
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        column = len(image[0])
        old_color = image[sr][sc]
        def helper(pixel_row, pixel_column):
            if image[pixel_row][pixel_column] == old_color:
                image[pixel_row][pixel_column] = newColor
                if ifValid(pixel_row+1, pixel_column):
                    helper(pixel_row+1, pixel_column)
                if ifValid(pixel_row-1, pixel_column):
                    helper(pixel_row-1, pixel_column)
                if ifValid(pixel_row, pixel_column+1):
                    helper(pixel_row, pixel_column+1)
                if ifValid(pixel_row, pixel_column-1):
                    helper(pixel_row, pixel_column-1)
            
        def ifValid(pixel_row, pixel_column):
            if pixel_row >= 0 and pixel_row < row and pixel_column >= 0 and pixel_column < column:
                return True
            return False
        if old_color == newColor:
            return image
        helper(sr, sc)
        return image
            
            