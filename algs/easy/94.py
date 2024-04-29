# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        stack = []
        curptr = root

        while curptr or stack:
            while curptr:
                stack.append(curptr)
                curptr = curptr.left
            curptr = stack.pop()
            res.append(curptr.val)
            curptr = curptr.right

        # def inorder(root):

        #     if not root:
        #         return

        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
            
        # inorder(root)
        return res