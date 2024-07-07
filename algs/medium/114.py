# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def dfs(node):
            if not node: return None
            if self.cur:
                self.cur.right = node
                self.cur.left = None
            self.cur = node

            right = node.right
            left = node.left

            dfs(left)
            dfs(right)
        
        self.cur = None
        dfs(root) 
                


        

"""
Relatively simple, just need to take time to think about the relationships 
and how nodes and references relate to eachother. 

Absolute base case outside of the recursion - if we don't have any nodes, return None

Recursive base case is if our current node is None, return None

Else check if we already have a cur (aka our builder representation)

For each node, set our right node to be equal to the next node in the pre order
traversal (which is going to be the node itself, followed by the node's left child, 
followed by the node's right child)



"""