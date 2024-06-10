class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


"""
Staple DP problem

We can break this problem up into subproblems after recognizing that at each index
we are either able to rob the current house, or not rob the current house and rob the 
next one instead. 

So here, we want to compute the max at the end of the array by incrementing the maxes
for each array as we traverse along.

Starting at 0, the max we can rob is nums[0]. 

At 1, the max we can rob is nums[0] or nums[1]

At 2, the max we can rob is either nums[1] assuming we robbed it previously,
or nums[0] + nums[2] because this gives us our gap. 

This logic of either taking the value at a previous index, or incrementing our value to be
two indices back + n allows us to build this sum up, and by the end of our run 
the final index will be calculated. 


"""