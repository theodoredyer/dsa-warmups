"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        otn = {}

        def dfs(node):

            if node in otn:
                return otn[node]

            new = Node(node.val)
            otn[node] = new
            for n in node.neighbors:
                new.neighbors.append(dfs(n))
            return new

        return dfs(node) if node else None
        

"""
Maintain a dictionary mapping for old nodes to new nodes

Set up a dfs that does the following:

(base case) 
If node is already in the mapping, return the node

(Normal)
If a node is not already in the mapping, create a newnode and a mapping, and
for each neighbor in the original node's neighbors, append the result of DFS on each 
of those neighbors to our new nodes neighbors. 

Note to check edge case of no existing nodes on input. 

"""