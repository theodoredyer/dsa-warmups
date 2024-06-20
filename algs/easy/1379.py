# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        dummy = cloned
        q = deque([dummy])
        tarval = target.val

        while q or dummy:

            for i in range(len(q)):
                dummy = q.popleft()
                if dummy:
                    if dummy.val == tarval:
                        return dummy
                    q.append(dummy.left)
                    q.append(dummy.right)
        
        return None
    

"""
just implement literally any graph search algorithm
"""