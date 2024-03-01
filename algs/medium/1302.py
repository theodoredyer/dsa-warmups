# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        storage = {}

        def dls(node, depth):
            if node is None:
                return
            
            if depth in storage:
                storage[depth].append(node.val)
            else:
                storage[depth] = [node.val]
            
            dls(node.left, depth+1)
            dls(node.right, depth+1)

        dls(root, 0)
        
        maxkey = 0
        for key in storage:
            if int(key) >= maxkey:
                maxkey = key
        
        return sum(storage[maxkey])
        