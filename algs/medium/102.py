# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            to_append = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    to_append.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if to_append:
                res.append(to_append)
        return res



"""
Level order traversal (parsing each level of the tree at a time) is the same thing as running BFS. 

Thus, this problem just boils down to running BFS but appending the values of each node in a level to some output array. 

The appending to the output array is trivial, except remember to not append new lists if those lists are actually just empty. 

For tree traversal (especially doing it iteratively) remember that we need some data structure to store the previous nodes that we need to continue to
iterate with, so when we traverse down to null, we know where to go back to. In the case of DFS this is often a stack, because that allows us to just go 
down one path, and pop up that same path all in a single row or straight path - this works because the order we traverse down in, is the same order we pop
back to the top in. 

For BFS this is a little bit different, because the order in which we hit the bottom of the tree is not the same and does not follow a vertical path, in 
order to keep the operation order we need to use a queue structure, so that we can process all of the nodes in a queue in each loop and then add each of 
the children for each node in the queue into the next loop. That looks like this:

q = collections.deque()
q.append(root)

while q:
    q_len = len(q)

    for i in range(q_len):
        node = q.popleft()
        do something with node
        add both of nodes children to q (might be empty)
    
    do something with the result of everything on this level of the tree

    continue to next level of tree

"""