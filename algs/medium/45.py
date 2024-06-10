class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return 0

        res = 0
        l = r = 0

        while r < len(nums) - 1:
            max_range = 0
            while l <= r:
                range_from_l = l + nums[l]
                max_range = max(max_range, range_from_l)
                l += 1
            r = max_range
            res += 1

        return res
            
        
"""
Break this problem up into batches, at each batch we want to see first if our 
right end of our batch is at the end of the array, we can return current jumps

If that is not the case, we want to calculate the window of all possible indices
we can reach from the current batch. We do this with the following logic

while we havent hit success condition
    jumps += 1
    max range this batch = 0
    while l <= r
        range from left = l + nums[l]
        max range this batch = max(max_range, range from left)
        increment left
    left (for next iteration) = current r + 1
    right (for next iteration) = max range this batch

until right pointer hits the end of the array. 


"""