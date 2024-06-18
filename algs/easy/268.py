class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for n in range(len(nums)):
            res = res ^ nums[n]
            res = res ^ n
        return res



"""
Any number xor'd with itself is going to return 0, and any number xor'd with 0 is going to return itself. 

Applying this logic, if we take 0 and xor it with everything in the array + all of the numbers that make up 
the range 1-n, we are going to be left with the one element that exists in the range, but not in the array. 



"""