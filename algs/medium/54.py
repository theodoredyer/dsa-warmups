class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        res = []

        while left < right and top < bottom:

            # Go right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Go down
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # Go left 
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Go Up
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

"""
(do you know how to use pointers in a 2d array 101)

just keep track of the boundaries we are able to search, and iterate through the 2d array 
in waves of going right, down, left, up. 

Tricky things to mention are always use right-1 and bottom-1 since we are keeping those pointers one index past the end of the array
to make other code simpler, and then also add the extra break check halfway through the loop (after we change top and right, and before 
we rely on top and right)


"""