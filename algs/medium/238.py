def productExceptSelf(nums):
        

    # [1, 2, 3, 4]
    # [24, 12, 8, 6]

    result = [None] * len(nums)

    # first pass
    # generate prefix values
    for i in range(len(nums)):
        if(i == 0):
            result[i] = 1
        elif(i == 1):
            result[i] = nums[0]
        else:
            result[i] = result[i-1] * nums[i-1]

    # second pass
    # generate postfix values
    i = len(nums) - 1
    postfix_factor = None
    for iterations in range(len(nums)):

        if i == len(nums) - 1:
            result[i] *= 1
            postfix_factor = nums[i]
        else:
            result[i] *= postfix_factor
            postfix_factor *= nums[i]

        i -= 1

    return result

productExceptSelf([1, 2, 3, 4])