class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}

        for fst, snd in edges:
            adj[fst].append(snd)
            adj[snd].append(fst)

        path = set()
        def dfs(cur, prev):
            if cur in path:
                return False
            path.add(cur)

            for conn in adj[cur]:
                if conn != prev:
                    if not dfs(conn, cur):
                        return False
            return True

        if not dfs(0, -1):
            return False
        else:
            return len(path) == n

            

"""
Basic graph traversal with DFS and undirected edges

For something to be a valid tree we just can't have loops, which is why we are tracking the
set of visited nodes as we go along, and tracking to see if we are about to process
another node that we've already seen and processed. 

KEY FEATURE HERE:
Need to pass the prev node through DFS to avoid going back to the same node with undirected 
edge that we just travelled from. 

Set up DFS with rules:
if node in visited path, return false. 
else, add node to visited path and dfs on every connecting node (EXCEPT PREV)
then return true

After running DFS on any node, if the list of connected nodes is less than n, 
we know that some amount of nodes are disconnected also making this an invalid tree
so return accordingly. 

"""