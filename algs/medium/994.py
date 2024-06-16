class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        num_rotten = 0
        max_time = 0
        rotten_q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    num_fresh += 1
                if grid[row][col] == 2:
                    num_rotten += 1
                    rotten_q.append((row, col, 0))

        time = 0
        seen = set()
        while rotten_q:
            r, c, curtime = rotten_q.popleft()
            if((r not in range(ROWS))
                or (c not in range(COLS))
                or (grid[r][c] == 0)
                or (r,c) in seen
                ):
                    continue
            if grid[r][c] == 1:
                num_fresh -= 1
                max_time = max(curtime, max_time)
            seen.add((r,c))
            for dr, dc in directions:
                rotten_q.append((r+dr, c+dc, curtime + 1))

        print(num_fresh)
        if num_fresh > 0:
            return - 1
        return max_time
            
            
"""
Standard graph BFS problem

To identify how long it takes for all of the fresh fruit to rot, you need to see 
for each fruit how fast it can infect the rest of the fruit. 

this is a classic "emanating from multiple nodes bfs" where we add all of the 
fruit to the queue and only start popping at the same time, so that we are processing
them all in the fastest possible layer for each location in the grid. For example if we instead
just ran bfs as soon as we encountered a rotten fruit, we would have to flip all the fruit 
for that BFS and ruin future runs if there are other rotten fruit closer to other 
fresh fruit nodes in the graph. 

Sort of a bad english explanation here but this problem is classic and should review it. 

"""