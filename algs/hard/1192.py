class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        critical_edges = []
        discovery = [0] * n
        lowest = [0] * n
        visited = set()
        self.time = 0

        adjacency = defaultdict(list)

        for s, e in connections:
            adjacency[s].append(e)
            adjacency[e].append(s)

        def dfs(cur, prev):
            visited.add(cur)
            self.time += 1
            discovery[cur], lowest[cur] = self.time, self.time

            for next in adjacency[cur]:
                if next not in visited:
                    dfs(next, cur)
                    lowest[cur] = min(lowest[cur], lowest[next])
                elif next != prev:
                    lowest[cur] = min(lowest[cur], discovery[next])
                if lowest[next] > discovery[cur]:
                    critical_edges.append([next, cur])
        dfs(0,-1)
        return critical_edges


"""
Might need to come back to this later to review tarjan's algorithm

"""