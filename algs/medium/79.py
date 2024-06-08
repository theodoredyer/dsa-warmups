def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        # tci = target character index (index of what we are looking for next)
        def backtrack(r, c, tci):
            if tci == len(word):
                return True
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS 
                or (r, c) in path
                or word[tci] != board[r][c]):
                return False

            path.add((r, c))
            
            res = (
                # Up
                backtrack(r-1, c, tci+1) or
                # Down
                backtrack(r+1, c, tci+1) or
                # Left
                backtrack(r, c-1, tci+1) or
                # Right
                backtrack(r, c+1, tci+1)
                ) 

            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True

        return False


"""
2-D Backtracking - fairly simple problem but need to pay attention to edge cases
and flow of logic, for a basic walkthrough:

For each index in our whole board, try to DFS from it:

Success base case:
is the index of the character we're looking for past the end of the length
of the word? if so we've already parsed the whole word, return true

Base case:
- are we at a valid index? (in bounds)
- are we at an index we're already visited in path?
- are we at the correct character?
^ If not, dip and go to next combination. 

If we are:
add current (r,c) to path

result = recurse for up, down, left, and right
remove current index from path, return result

Time complexity = n*m to search all start characters * dfs
so n*m*4^n

"""