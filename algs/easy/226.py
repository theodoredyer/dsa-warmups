# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dummy = root
        # q = deque()
        # q.append(root)

        # while q or cur:
        #     for i in range(len(q)):
        #         cur = q.popleft()
        #         if cur:
        #             q.append(cur.left)
        #             q.append(cur.right)
        #             tmp = cur.right
        #             cur.right = cur.left
        #             cur.left = tmp

        # return dummy
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



"""
Easiest tree problem, can be implemented with BFS or recursively (maybe dfs? idk) 

For bfs it is standard bfs traversal except for each node we encounter we attempt to swap its children and then add the children as normal
the recursive solution I find a little bit more complicated in terms of references but it follows a simple pattern:

base case = current is null, return None
else flip current node's left and right then recursively call on left and right - I guess in place changes are what allows this to work
"""