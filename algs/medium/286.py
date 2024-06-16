class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited_chests = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r,c):
            seen_from_this_chest = set()

            q = deque()
            q.append((r,c, 0))

            while q:
                r, c, dist_to_chest = q.popleft()

                if ((r not in range(ROWS)) or 
                   (c not in range(COLS)) or 
                   ((r,c) in seen_from_this_chest) or 
                   (grid[r][c] == -1)):
                    seen_from_this_chest.add((r,c))
                    continue
                    
                grid[r][c] = min(grid[r][c], dist_to_chest)
                seen_from_this_chest.add((r,c))

                
                for d in directions:
                    q.append((r + d[0], c + d[1], dist_to_chest + 1))
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    bfs(row, col)
        return grid

"""
Bit of a trickier graph bfs/dfs with needing to track some external variables:

standard process but a lot easier if we rephrase the question:
in order to find closest distance to each chest from each node in the graph
we should instead take each chest, and expand from each chest to see how far each node is 
away from each chest, taking the minimum in between different chests. 

This one is just a bit tricky for maintaining the distance to each chest in between
queue layers, just remember to track the distance as a third queue element instead of
trying to do it iteratively. 


"""