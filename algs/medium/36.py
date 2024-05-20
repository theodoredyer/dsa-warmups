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