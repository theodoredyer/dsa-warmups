class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        directions = [1, 0], [-1, 0], [0, 1], [0, -1]

        def bfs(r,c):
            
            island_size = 0
            q = deque()
            q.append((r,c))

            while q:
                r, c = q.popleft()
                if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in seen:
                    continue
                if grid[r][c] == 1:
                    seen.add((r, c))
                    island_size += 1
                for dim in directions:
                    q.append((r + dim[0], c + dim[1]))
            return island_size

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, bfs(row, col))

        return max_area
            

"""
Standard DFS or BFS traversal of a graph

Keep track of max island seen so far, and whenever we encounter an island when
parsing through all rows and columns we want to traverse through that whole 
island with either bfs or dfs and add the elements we've already seen to a set 
to make sure we don't revisit islands twice. Return from this BFS or DFS the actual
size of the island we just scraped through and then continue iterating through
the rest of the islands finding which ones might be bigger than our current. 

"""