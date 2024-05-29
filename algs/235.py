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