class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, visitset, lastHeight):

            if(
                r not in range(ROWS)
                or c not in range(COLS)
                or (r,c) in visitset
                or heights[r][c] < lastHeight
            ):
                return
            
            visitset.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visitset, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


"""
Fairly tricky DFS problem. 

In order to avoid calculating from every position if we can reach both other 
sides of the grid, we want to instead start from the edges of the grid and 
see how many nodes we can reach from each edge. 

For left and top edges, we add these nodes we can reach to the PAC set, and for
bottom and right we use the ATL set. 

After populating these we take a union of the two sets and return the nodes that 
are able to reach both coasts. 

"""