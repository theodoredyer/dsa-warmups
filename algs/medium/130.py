class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        visited = set()

        def dfs(r, c):
            if(
                r not in range(ROWS)
                or c not in range(COLS)
                or (r,c) in visited
                or board[r][c] == "X"
            ):
                return
            visited.add((r,c))
            board[r][c] = "S"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        # Scan top row
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)

        # Scan bottom row
        for c in range(COLS):
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)

        # Scan left column
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)

        # Scan right column
        for r in range(ROWS):
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "S":
                    board[row][col] = "O"

        return board 

        

"""
Tricky dfs problem here - no shot I'm thinking of this solution on the spot. 

Simple part is needing to identify that a region is unsurrounded if and only 
if one section of that region touches one of the edges of the board, otherwise it
by nature is just surrounded by Xs. 

After seeing this, we need to do one pass around the edges marking all of the regions that 
can be touched by Os on the edge as temporarilly "S" or Safe/unsurrounded. 

After doing this we flip all the remaining Os to Xs, and then in a second pass, flip the 
Ss to Os. 

"""