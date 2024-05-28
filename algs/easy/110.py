# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, -1]

            hl = dfs(node.left)
            hr = dfs(node.right)

            balanced = (hl[0] and hr[0] and abs(hl[1] - hr[1]) <= 1)

            return [balanced, (max(hl[1], hr[1]) + 1)]

        return dfs(root)[0]


"""
Fairly standard tree DFS problem, the thing we need to track is for each node, if the height of the left child branch and right child branches differs by 
no more than 2, if it does we propagate False back to our solution. 

The tricky part of this question comes in the fact that we need to return two things from each subtree, that being the status check of the tree being
balanced so far, alongside the height of the current tree. we do this to make sure that if a subtree was invalid but the height of that subtree satisfies
the conditions for a higher tree's validity, we still make sure the fact that it was actually wrong underneat that umbrella is known to the larger scope. 
"""