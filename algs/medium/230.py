# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        counter = 0
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            counter += 1
            if counter == k:
                return cur.val
            cur = cur.right


"""
This problem is essentially just inorder traversal of a tree, with bringing along a counter variable to figure out when we've reached the kth element. 

The inorder traversal traverses to the smallest element, and then up through the tree, we did this iteratively using a stack to keep track of the parents
of nodes, and generally speaking the traversal follows this pattern:

cur = root
stack = []

while cur or root:
    while cur:
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    (num_nodes_visited += 1)
    if we have visited k nodes, return cur.val
    cur = cur.right


"""