# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        # BFS Solution
        q = deque([root])
        cur = root
        max_depth = 0
        level = 0

        while q:
            level += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    max_depth = max(max_depth, level)
                    q.append(cur.left)
                    q.append(cur.right)

        return max_depth


        # Recursive solution
        """
        if not root:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
        """



"""
Choose any tree traversal algorithm and then have a corresponding way to track the level of the tree you're at, and make checks along the way
to see if that level is a new max depth. 

Simplest with recursion, BFS also simple, DFS requires sort of a tricky modification to the actual stack to also track current level.
"""