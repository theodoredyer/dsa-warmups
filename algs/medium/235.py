# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qval = q.val
        pval = p.val

        cur = root

        while cur:
            curval = cur.val

            if pval > curval and qval > curval:
                cur = cur.right
            elif pval < curval and qval < curval:
                cur = cur.left
            else:
                return cur


"""
This problem just relies on you to identify the criteria for traversal, in order to determine if we can go a node lower than our current node, we need to 
evaluate some items:

if p and q are both less than current, then we know we can look left further, because clearly there must be a node less than or equal to p and q to the left
similar case with when p and q are both greater than current. 

if that neither of those conditions are met, then that means we must currently be sitting at the split point between these two nodes, where if we went left
then we are no longer an ancestor of the right side, and similarly if we went right we are no longer an ancestor of the left side, thus we are currently 
as low as we are able to go while maintaining the criteria. 
"""