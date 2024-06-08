# Backtracking
## Explanation
Like trying to solve a maze by exploring all possible paths. When we reach dead ends we backtrack (go abck to previous decision point) and try a different path
- Choose: make a choice from the available options
- Explore: recursively explore the choice further
- Un-choose: if the choice leads to dead ends (hits base cases), undo the choice and try another.
### General Runtime
For ones I've done so far, we are creating 2 possibilities for each element (include or not include) which generally results in 2^n, generally speaking adding a sorting step doesn't add considerable runtime. 
## When to Use
- Combination and permutation problems, when we need to generate combinations, permutations or subsets. 
- Constraint satisfaction problems (sudoku, crosswords)
- Pathfinding problems, when we need to explore paths in a grid or graph (maze solving etc)
- Decision-Making problems, when each decision leads to a new set of choices, and we need to explore them to find a valid or optimal solution. 
## Templates

### Case - 1D we need to avoid duplicates
- Often times we need to create combinations where we need to avoid duplicates:

Problem(array, target):
    results = []
    array.sort() (because runtime is likely more than nlogn)

    def backtrack(index, subarray):
        if condition == target:
            results.append(subarray[::])
            return
        if index == len(array):
            return

        # Case 1, include i as an option
        subarray.append(array[index])
        backtrack(index + 1, subarray)

        # Pop to set up case 2
        subarray.pop()

        # Case 2, dont include i as an option
        
        # Optional, if no duplicates, skip to next instance that isnt nums[i]
        while index + 1 < len(array) and array[index] == array[index + 1]:
            index += 1

        backtrack(index + 1, subarray)

    backtrack(0, [])
    return results

### Case - 2D Search for a pattern in a matrix
Problem(matrix, target_list_or_word):

    visited_path = set()

    def backtrack(r, c, INV):
        # INV = index of value we're looking for
        if INV == len(target_list_or_word):
            return True
        if (
            r < 0 or c < 0 or r >= ROWS or c >= COLS
            or (r,c) in visited_path
            or matrix[r][c] != target[INV]
        ) return False

        visited_path.add((r,c))

        result = (
            backtrack(r-1, c, INV+1)
            or backtrack(r+1, c, INV+1)
            or backtrack(r, c-1, INV+1)
            or backtrack(r, c+1, INV+!)
        )

        visited_path.remove((r,c))
        return res

    for (all possible indices)
        if backtrack(r,c,0):
            return True
    return False













# Problem Type

## Explanation

### General Runtime

## When to Use

## Templates

