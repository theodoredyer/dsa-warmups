class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # option 1
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # option 2
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res

            

"""
Backtracking problem - when considering a route to go for continuing to add values, we want to either add the current value again, or never add the current 
value ever again in order to avoid ever implementing duplicates. 

So the approach for this is recursive:

base cases:
- total of current consideration = target? add current to the valid combos and return
- total is bigger than target? return 

recurse on current with another copy of i
recurse on current with the next value in the candidates list

Need to make sure we are appropriately manipulating the current array before recurring. This is done by making the appending of the current value
at index i, and then popping it before the second recursive call.

"""