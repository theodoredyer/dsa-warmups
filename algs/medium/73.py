class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rowzero = False

        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == 0:
                    matrix[0][k] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowzero = True
                    

        for i in range(1,len(matrix)):
            for k in range(1,len(matrix[0])):
                if matrix[0][k] == 0 or matrix[i][0] == 0:
                    matrix[i][k] = 0

        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        if rowzero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        return matrix
        

"""
Various approaches, and they all rely on the concept that we can't just immediately modify the matrix in place, because we would
create extra zeroes and then blank out the entire matrix. 

So option 1 (worst) would be to create a whole duplicate matrix, and 0 out all of the rows as we otherwise would, while we scan through the original
and continue to check logic just based on the original (this is m*n)

Option 2 = keep a list for the rows and columns we need to 0 out, and then do that in a pass later (m+n)

Option 3 =  just have the actual 0 index row and 0 index column serve this purpose ^ and keep an extra variable for the (0,0) square since it needs to 
hold info for both rows and columns. 

"""