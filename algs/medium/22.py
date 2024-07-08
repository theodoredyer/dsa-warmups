class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0,0)
        return res


"""
generate permutations/combinations == recursive backtracking 100%

Base cases are if our total number of parentheses are met for both open
and closed, append our result, otherwise if we can add an open parenthesis
(where open < n) then append ( to stack, and recurse. 

"""