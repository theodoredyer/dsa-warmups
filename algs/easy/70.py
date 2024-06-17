class Solution:
    def climbStairs(self, n: int) -> int:
        
        stl = 1
        las = 1

        for i in range(n-1):
            i = stl + las
            tmp = stl
            stl = i
            las = tmp

        return stl



        
"""
Dynamic programming (but simple)

Starting from the end of the staircase, we know there is only one way to end up at the last stair (just existing there), 
also there is only one way to end up at the last stair from the second to last stair, because you can only jump 1 stair, jumping 
2 would result in you jumping out of bounds.

So from here, each preceeding stair is made up of all of the ways you can get to the end after jumping 1 stair + all of the ways 
you can get to the end after jumping 2 stairs. 

So just iterate backwards through the list and keep incrementing the amount of stairs i takes by just adding the two options you have to 
jump to from i

This problem doesn't require auxilary caching structure or anything because of the fact that to calculate the state for one step we only need to 
know the states of the previous two steps. For example some other DP problems would have deeper nested dependencies on previous states. 

"""