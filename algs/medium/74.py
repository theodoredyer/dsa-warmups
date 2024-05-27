class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Search for the row:
        top, bottom = 0, num_rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            row_start = matrix[mid][0]
            row_end = matrix[mid][num_cols - 1]

            if target > row_end:
                top = mid + 1
            elif target < row_start:
                bottom = mid - 1
            else:
                break
        
        if top > bottom:
            return False
        else:
            row = (top + bottom) // 2

        l, r = 0, num_cols - 1
        while l <= r:
            m = (l + r) // 2

            midval = matrix[row][m]

            if midval == target:
                return True
            elif midval > target:
                r = m - 1
            else:
                l = m + 1

        return False



"""
This problem should be immediately identified as a 2x binary search problem, we need to search a structure that is sorted in two dimensions, so we just
apply the principles of binary search to both of these dimensions. 

the tricky part of this problem is identifying the exact criteria/edge case rules for the first binary search, because we are trying to find the exact row
that the value is in, the approach should be to pick the mid row, if the start of our mid row is greater than our target, move up, if the end of our mid row
is less than the value of target, move row down, else we are in our row. 

then its simple binary search from there

"""
