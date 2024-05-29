# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr, curr_max_seen):
            if not curr:
                return 0

            is_curr_good = 1 if curr.val >= curr_max_seen else 0
            new_max = max(curr_max_seen, curr.val)
            return is_curr_good + dfs(curr.left, new_max) + dfs(curr.right, new_max)

        return dfs(root, root.val)


"""
This problem requires us to calculate the number of nodes for which the path from that node to the root meets some criteria, when we are looking straight
vertically like this from child nodes back to the root, DFS seems appropriate, considering we don't care about values on other branches at all. 

Also note that we are doing this pre-order, because the value of a node being good doesn't depend on its children, it only depends on itself and the values
above it, so when we are doing our recursive call its going to look like this:

base case
process_current
process_children

I believe this could be done iteratively with a stack and DFS, but this solution is using recursion with the following rules:

if our node is null, return 0
if our node is good, result += 1
return result + dfs(left) + dfs(right)

"""