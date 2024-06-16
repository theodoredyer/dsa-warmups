class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


"""
Tricky DFS problem, need to revisit at some point in the future. 

Start by setting up an adjacency map to outline all of the connections between courses 
and corresponding prerequisites. 

Next, recurse through every node with the following dfs criteria:

- add course to our 'visit' set or outgoing travel set
- if course has no prereqs, return true.
- if course has multiple prereqs, recurse for each of them, returning false if they 
return false because we want to propagate potential failures back up to the top level
- after recursing through all children, remove the parent from visit set (aka remove current)
and clear out the adjacency map from current set, because we want it to return true since
we know the current course can be completed and want to echo that to future calls to this node

and then call this dfs function on every node. 

"""