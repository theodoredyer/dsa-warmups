class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(idx):
            if idx in safe:
                return safe[idx]

            safe[idx] = False
            for nbr in graph[idx]:
                if not dfs(nbr):
                    return safe[idx]
            safe[idx] = True
            return safe[idx]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)

        return res
