class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lst = cost[len(cost) - 1]
        stl = cost[len(cost) - 2]

        for i in range(len(cost) - 3, -1, -1):
            nxt = min(lst, stl) + cost[i]
            cost[i] = nxt
            lst = stl
            stl = nxt

        return min(cost[0], cost[1])