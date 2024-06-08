class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, subset):
            if sum(subset) == target:
                res.append(subset[::])
                return
            
            if index == len(candidates) or sum(subset) > target:
                return

            # try combos including candidates[i]
            subset.append(candidates[index])
            backtrack(index + 1, subset)
            subset.pop()

            # try combos not including candidates[i]
            while (index + 1 < len(candidates)) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res


"""
Standard backtracking problem, with duplicate detection case. 

Need to start by sorting the input, because we know our number of potential combinations
is 2^n, and each combination can be n numbers long, adding a nlog(n) operation into our 
n2^n complexity solution isn't going to be consequential. 

Sorting our input allows us to avoid recurring into duplicate solutions, because of the following
logic:

if we are following the backtracking pattern of:

def backtrack(index, subset):

if we meet our criteria:
    append subset[::] to result
    return

if we are out of bounds:
    return

recurse for subsets including array[i]

recurse for subsets not including any instance of array[i]
(accomplish this by incrementing index out of range ie line 20)

backtrack from start

time complexity is again n2^n

"""