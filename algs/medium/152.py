def maxProduct(self, nums):

    maxprod = max(nums)

    current_max = 1
    current_min = 1

    for num in nums:
        if(num == 0):
            current_max = 1
            current_min = 1
            continue
        else:
            tmp = current_max
            current_max = max(num * current_max, num * current_min, num)
            current_min = min(num * tmp, num * current_min, num)

        maxprod = max(current_max, maxprod)

    return maxprod
