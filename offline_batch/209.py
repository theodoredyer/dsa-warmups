def minSubArrayLen(target, nums):
    running_sum = 0
    lptr = 0
    res = float("inf")

    for rptr in range(len(nums)):
        running_sum += nums[rptr]

        while running_sum >= target:
            res = min(rptr - lptr + 1, res)
            running_sum -= nums[lptr]
            lptr += 1

    return 0 if res == float("inf") else res



