# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Notes
        # Diameter = Height(L) + Height(R) + 2
        # Height = Max(L, R) + 1

        max_diam = 0

        def dfs(node):
            nonlocal max_diam

            if not node:
                return -1
            hl = dfs(node.left)
            hr = dfs(node.right)

            max_diam = max(max_diam, (hl + hr + 2))
            return (max(hl, hr) + 1)

        dfs(root)
        return max_diam



"""
This problem, when broken down is a relatively simple recursion problem, where you just need to remember two equations or concepts:

the height of a null tree is -1, and the height of any other tree is: max(height(left), height(right)) + 1
this +1 comes from the fact that we are already +1 above both the left and the right to get to current node. 

And the next equation to remember is the equation for diameter, which is built up recursively and is:
(HL + HR + 2)

This works, because the +2 implies the connection to right and left are two valid connections, but when one of those heights is actually null, that -1 value
for null tree height balances this back out to being accurate. 


"""