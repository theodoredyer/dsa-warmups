class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = {i:[] for i in range(numCourses)}
        res = []

        for crs, pre in prerequisites:
            adj_map[crs].append(pre)

        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in res:
                return True

            cycle.add(crs)

            for pre in adj_map[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            

"""
Somewhat involved DFS problem (topological sort)

First, set up adjacency map so we know how to traverse when doing DFS and what nodes
we need to visit. 

set up visit set to track cycles
set up result list

DFS should be the following:
- if course is in visit set, return false. 
- if course is in result list, return true
- add current course to visit set
- for prerequisite in our map DFS the prereqs, return false if any of them do to propagate
any failure states internally with courses not functioning. 
- remove current from cycle and append it to res if all of the others return true. 
- run this dfs on every node. 

"""