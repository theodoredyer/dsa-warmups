# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []

        while q:
            qlen = len(q)
            furthest_this_row = None
            for i in range(qlen):
                cur = q.popleft()
                if cur:
                    furthest_this_row = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if furthest_this_row:
                res.append(furthest_this_row.val)
        return res


"""
In order to find only the nodes visible when looking at the tree from the side, we need to recognize that this is a BFS problem, where we are looking for
the element at the far edge of each layer of our BFS. Naturally we just use a queue and traverse accordingly. 

The only tricky parts to note here are for the edge cases, make sure we are not trying to access values of None nodes, etc. 
"""