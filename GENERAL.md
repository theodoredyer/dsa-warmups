# General
- If we need to track a list, suppose a list of user_ids that someone is following for a twitter clone and we want to be able to add and remove in constant time, use a set instead of list, or for tracking all of the users of a system "user1 follows u2, u3, u4" "user 2 follows u4" etc, use a hashset with key = user, val = hashset of followees
- Sets use [setname.add / setname.remove] not append
- To sort a list of entities by something other than just pure value: "thing.sort(key=lambda i: i[1])"
- When doing BFS where we need to track distance from the origin, pass that as a parameter through the element of the queue - way easier to not have tricky situations if we do this. 
- With undirected graph traversal, pass the previous node through DFS to avoid trying to jump back to the exact same edge since the connection is shared. 

### Adjacency Maps
Undirected:
```python
def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}

        for fst, snd in edges:
            adj[fst].append(snd)
            adj[snd].append(fst)

Directed:
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
```

Review:
- M 133
- M 207


#### ==================================================================
# Sliding Window

## Explanation
Used to perform a required operation on a subset of data within a larger set. Maintain a window of elements that moves or slides through the data structure to process the data structure in segments. 

- Some use fixed sized windows (otherwise this is just standard two pointer) and determine the direction of the slide on some criteria
- Some use dynamic sized windows, changing based on certain criteria. 


### General Runtime
- Often O(n) or O(nlogn) if we are iterating through a list, and potentially needing to sort it. 

## When to Use
- Contiguous subarrays or substrings: if we need to find or process some contiguous parts of an array or string, sliding window is likely. 
- Sum, average, or max/min in subarrays
- Character patterns: solving patterns or substrings without repeating characters etc. 

## How to solve
- Identify application, do we have some contiguous subsection to work with or find?
- Determine window type, dynamic or fixed size based on problem
- Init variables for tracking the state of the window and its contents. 
- Slide the window by adjusting pointers and modifying window state accordingly based on whatever internal criteria we are tracking. 

## Common pitfalls
- Boundary conditions and empty inputs
- Clear and concise initialization of window and properties. 
- Efficient updates and scanning criteria. 


## Templates
#### ==================================================================
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            window_len = r - l + 1
            count[s[r]] = 1 + count.get(s[r], 0)

            while max(count.values()) + k < window_len:
                count[s[l]] -= 1
                l += 1
                window_len -= 1
            
            longest = max(longest, window_len)
        return longest
```
#### ==================================================================
# Two Pointer

## Explanation
Similar to a simpler sliding window, we don't necessarilly need to track state of a whole range of values. 

### General Runtime
- Lots of O(N) applications with some nlogn if we're sorting to effectively use a two pointer setup. 

## When to Use
- Problems involving pairs of elements or comparing elements from both ends of a list
- Benefit from sorting or if lists are already sorted. 

## How to solve
- Use two pointers to traverse an array from different ends, adjusting pointers based on certain criteria to arrive at a solution. 

## Templates
#### ==================================================================




#### ==================================================================
# Greedy Algorithms

## Explanation
Build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. The idea is that local optimization leads to global optimization.

## When to Use
- Optimization problems: if we need to max or min a certain criteria or value (maximum activities, min cost) etc. 
- Choices and constraints: When each step involves making a choice that could impact some overall outcome. 
- Comparative selection: problem involves selecting items based on a certain comparison (smallest, largest, etc).

## How to solve
- Understand the problem, clarify objective and any extraneous factors that can limit greedy's applicability. 
- Identify the greedy strategy (criteria for optimal choices)
- Implement the rest of the algorithm (sort if needed for greedy, track vars, rest of logic etc). 

## Common pitfalls
- Unsorted input
- make sure nlogn is suitable in order to use sorting. 


### Examples
- Activity selection: selecting max number of activities that dont overlap with start and end times (sorting and then iteration)
- Huffman coding: Create a binary tree for optimal prefix codes based on frequency of characters. 



## Templates
#### ==================================================================



#### ==================================================================
# Dynamic Programming

## Explanation
Method for solving complex problems by breaking them down into simpler subproblems. It is applicable to problems exhibiting the properties of overlapping subproblems (problem can be broken down into smaller, reusable subproblems) & optimal substructure (the optimal solution to a problem can be constructed from the optimal solutions of its subproblems).

### Approach
- Define the state, determine what each subproblem represents in terms of variables
- State transition, establish how to compute the solution of a subproblem using solutions of smaller subproblems
- Base case, define the simplest subproblems with a known solution. 
- Memoization or tabulation: store results of subproblems to avoid redundant computations. 

### General Runtime

## When to Use
- Finding maximum, minimum, or optimal solution (shortest path, maximum profit)
- Counting problems: number of ways to do something (counting paths, combinations)
- Decision problems: sequence of decisions to achiev an optimal outcome


## Templates
#### ==================================================================
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for curamt in range(1, amount + 1):
            for c in coins:
                if curamt - c >= 0:
                    dp[curamt] = min(dp[curamt], 1 + dp[curamt - c])

        return dp[amount] if dp[amount] != (amount + 1) else -1
```

#### ==================================================================
# Binary Search

## Explanation
Efficient algorithm for finding an element in a sorted list of items. Works by shrinking the search criteria while guessing for a value. 
- Requires sorted input
- Utilizes divide and conquer


### General Runtime
O(log(n))

## When to Use
- Sorted Input: problems involve a sorted array or list
- Search Optimization
- Monotonic functions: problems where a function is strictly increasing or decreasing. 


## Templates
```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```
#### ==================================================================




#### ==================================================================
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

```python
Problem(array, target):
    results = []
    array.sort() (because runtime is likely more than nlogn)
  b
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
```

### Case - 2D Search for a pattern in a matrix
```python
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
            or backtrack(r, c+1, INV+1)
        )

        visited_path.remove((r,c))
        return res

    for (all possible indices)
        if backtrack(r,c,0):
            return True
    return False
```
#### ==================================================================




#### ==================================================================
# Graphs

## Explanation
Data structures consisting of nodes and edges, used to model relationships and pathways such as networks, maps, socials. 

- Consists of vertices and edges, or coordinates in a plane. 
- Edges can be directed or undirected, and weighted or unweighted. 
- 

### General Runtime

## When to Use
- Network relationships - problems involving pathways or relationships
- Traversal requirements - checking or visiting nodes and validating connectivity. 
- Optimization - optimal paths or structures

## How to solve
- Identify components like graph structure, weighted/unweighted, directed/nondirected, etc. 
- Determine the most suitable algorithm for the problem type (traversal, shortest path, MST). 
- 

## Templates
```python
def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    result = []

    def dfs_recursive(node: int):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            dfs_recursive(neighbor)

    dfs_recursive(start)
    return result
```

### Multi-point BFS (radiate from multiple nodes)
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        num_rotten = 0
        max_time = 0
        rotten_q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    num_fresh += 1
                if grid[row][col] == 2:
                    num_rotten += 1
                    rotten_q.append((row, col, 0))

        time = 0
        seen = set()
        while rotten_q:
            r, c, curtime = rotten_q.popleft()
            if((r not in range(ROWS))
                or (c not in range(COLS))
                or (grid[r][c] == 0)
                or (r,c) in seen
                ):
                    continue
            if grid[r][c] == 1:
                num_fresh -= 1
                max_time = max(curtime, max_time)
            seen.add((r,c))
            for dr, dc in directions:
                rotten_q.append((r+dr, c+dc, curtime + 1))

        print(num_fresh)
        if num_fresh > 0:
            return - 1
        return max_time
```
#### ==================================================================




#### ==================================================================
# Trie

## Explanation
Similar to basic tree but used specifically for words

### General Runtime
Used for O(26*n) time lookups

## When to Use
Fairly standout - when we need to look up / store strings for autocomplete/spellcheck, implementing dictionaries, sorted retrieval, 

## Templates
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if len(curr.children) == 0:
            return curr.endOfWord
        return True
```
    

#### ==================================================================

#### ==================================================================
# Heap / Priority Queue

## Explanation
- Can be illustrated as a nearly complete binary tree, or an array. 
- Max heap = for a given node i, i.val is greater than or equal to val of all of its children, reverse this for min heap. 
- When heaps are represented as an array:
[21, 17, 15, 14, 9, 12, 13, 8, 5, 1]

To access a node's left child: index * 2
To access a node's right child: index * 2 + 1
To access a node's parent: floor(index / 2)

- Height is O(log(n))
- Priority queue is similar to a regular queue or stack, but is an abstract data type and each element has a priority, where elements are then dequeued according to their priority. 

### General Runtime
- Insertion = O(log n)
- Deletion = O(log n)
- Peek = O(1)
- Build heap = O(n)

## When to Use
- Scheduling tasks - when tasks need to be processed in order of priority
- Graph algorithms - Used in Dijkstra's and Prim's for finding shortest paths and minimum spanning trees. 
- Event Simulation - Managing events in simulations where events need to be processed based on their scheduled time. 
- Real-time systems - for handling real time tasks with varying priorities


## Templates
#### ==================================================================
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        curtime = 0
        q = deque()

        while maxHeap or q:
            curtime += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1

                if count != 0:
                    q.append([curtime + n, count])
            
            if q and q[0][0] == curtime:
                entity = q.popleft()
                heapq.heappush(maxHeap, entity[1])

        return curtime
```





#### ==================================================================
# Problem Type

## Explanation

### General Runtime

## When to Use

## Templates
#### ==================================================================

