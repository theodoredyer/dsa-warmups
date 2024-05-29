# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def sameTree(self, r1, r2):
        if not r1 and not r2:
            return True
        
        if r1 and r2 and r1.val == r2.val:
            return self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right)

        return False



"""
This problem is pretty tricky compared to other easy tree problems and involves writing two recursive functions. 

First we set up a helper function to determine if two trees are the same taking in the roots as params and recursively going through each 
of the trees comparing them at each step

Second we set up the main function, and make the following checks:
- if our subtree is empty, return true because that means no matter what it is a part of the main tree, main trees always have empty child nodes. 
- if our main tree is empty, return false because that means we have already parsed through to check the subtree, and the main is already empty. so the
        subtree must be bigger than main tree
- if neither of these cases, check if the trees are the same. if they are return true
- if the trees are not the same, check if the children of main tree are the same as subtree. 
"""