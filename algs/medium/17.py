class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }

        def backtrack(i, substr):
            if i == len(digits):
                if len(substr) > 0:
                    res.append(substr[::])
                return
            
            cur_num = digits[i]
            for element in mapping[cur_num]:
                backtrack(i+1, substr + element)
            
        dfs(0, "")
        return res


"""
Standard backtracking problem, for each index we want to explore all possible 
combinations for future paths (indicated by the range of values for each number)
and once we reach our base case we simply return. 

The only thing to really note with this backtracking problem is we don't realy need
to keep track of a running subset and pop any changes made to it, because we are sort of 
doing a BFS type approach where we are create all possible substrings for each index 
as we arrive at that index. 

if the index we're looking at is at the end of the length of input
- add our current substring to res

else:
- run a recursion for all possible substrings of current value


"""