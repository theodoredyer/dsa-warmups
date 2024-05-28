# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True

            if node.val >= right or node.val <= left:
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))



"""
The only real thing we're doing here is recursively checking whether or not all of the nodes of a tree meet the criteria for the tree to be valid, meaning
that all of a node's left children are less than itself, and its right children are greater than itself. 

This problem is essentially just DFS, with the caveat that we are continuing to populate down the boundaries (left bound and right bound) that each node
beneath the current is allowed to be.

Empty nodes return true, otherwise return the result of checking that boundary
"""