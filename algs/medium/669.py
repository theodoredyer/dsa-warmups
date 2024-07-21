# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        rootval = root.val
        if rootval < low:
            return self.trimBST(root.right, low, high)
        elif rootval > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


"""
Standard recursive tree problem

Basic logic is that if a node is greater than our max value, clearly it doesn't
belong in the result tree, nor does its right children. So because of this 
we instead just return our left child in hopes that future recursive calls work for that child

Same thing for if we are smaller than the minimum, we will just pass along the right child
in hopes it is larger than the min. 

If our current root is fine, just run the same checks on both of its children. 

"""