class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        right = len(matrix) - 1
        left = 0

        while left < right:
            for i in range(right-left):
                top, bottom = left,right

                tmp = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = tmp
            right -= 1
            left += 1


"""
Set up pointers for right and left, and the idea is to rotate iteratively sending the top left value to top right, 
top right to bottom right, br to bl, bl to tl. 

Much easier to understand drawing it out visually. 

Note right pointer is -1 from cols because we don't actually need to rotate the TR value, it is getting replaced by the TL value from the same run. 


"""