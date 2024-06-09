def maxSubArray(nums):

    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sum = max(max_sum, cur_sum)

    return max_sum



print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([5, 4, -1, 7, 8]))


"""
To calculate max subarray, just traverse forwards seeing if the current
accumulation is greater than the max, if we ever arrive at a point where
we are at accumulation < 0, just reset to 0 because we're allowed to ignore
sections of the array that don't contribute positively. 

after resetting to 0, continue to check to see if we can find a greater max,
checking at each iteration if we're at a new max. 

"""