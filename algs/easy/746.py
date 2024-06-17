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

"""

Similar to the standard climbing stairs question, need to recognize that this is a DP problem
that has a state only depending on two other states, thus don't really need any auxilary data structure. 

We start from the back of the list where the cost to reach the end from the last two nodes is just those two nodes themselves
because for each we can either just jump 1 to the end (or if we are 2 steps back, jump 2)

from here on out, for each step the cost to reach the end is the cost of that step + the minimum of the two options it has from 
there. Just iterate back through the start of the list and return min at index 0 or 1

"""