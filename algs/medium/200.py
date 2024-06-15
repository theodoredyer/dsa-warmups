class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        seen = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            

            while q:
                r, c = q.popleft()
                up = [r-1, c]
                down = [r+1, c]
                left = [r, c-1]
                right = [r, c+1]

                if r >= ROWS or c >= COLS or r < 0 or c < 0 or ((r, c) in seen):
                    continue

                if grid[r][c] == "1":
                    seen.add((r,c))
                    q.append((up[0], up[1]))
                    q.append((down[0], down[1]))
                    q.append((left[0], left[1]))
                    q.append((right[0], right[1]))

            return 0

            

        def dfs(r, c):
            up = [r-1, c]
            down = [r+1, c]
            left = [r, c-1]
            right = [r, c+1]

            if r >= ROWS or c >= COLS or r < 0 or c < 0 or ((r, c) in seen):
                return 0
            if grid[r][c] == "1":
                seen.add((r,c))
                dfs(up[0], up[1])
                dfs(down[0], down[1])
                dfs(left[0], left[1])
                dfs(right[0], right[1])
        

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in seen:
                    continue
                if grid[r][c] == "0":
                    continue
                else:
                    num_islands += 1
                    bfs(r, c)
        return num_islands


"""
Contains both BFS and DFS solutions for practice, but the concept is simple:

iterate through each element until we find a 1, once we do, we want to scan the whole
grid and add all of the elemnts of this island to our set of seen items so we don't repeat
ourself later and double count an island. 

After flagging all seen pieces of our island, continue looking for new incides with new islands


"""