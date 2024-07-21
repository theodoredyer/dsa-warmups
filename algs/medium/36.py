class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for k in range(9):
                val = board[i][k]

                if val == ".":
                    continue

                if val in rows[i] or val in cols[k] or val in squares[(i//3, k//3)]:
                    return False

                rows[i].add(val)
                cols[k].add(val)
                squares[(i//3, k//3)].add(val)

        return True
    
"""
Simple problem, just set up a dictionary for each row, column, and square
and when iterating through the whole array, if we encounter an item that is already in 
one of these then we know we broke a rule and should return false. 

the coordinate for the 'square' is the index // 3

also for the square dictionary make the key a tuple since we can't do list



"""