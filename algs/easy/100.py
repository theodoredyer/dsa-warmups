# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False


"""
For this problem in order to determine if two trees are the same, just run DFS and compare the nodes of each at each step as we go down
the only tricky part of this problem is edge cases and making sure we're only trying to access values of trees if we know they exist etc

Simple way to blanket statement this is:
- if both nodes are None, return true
- if both nodes are NOT None, and are equiavlent (making sure both are not none before accessing values of both), return true
- else false
"""