class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        else:
            return max(self.hr1(nums[1:]), self.hr1(nums[:-1]))


    def hr1(self, nums):
        r1, r2 = 0, 0

        for n in nums:
            nmax = max(r1 + n, r2)
            r1 = r2
            r2 = nmax
        
        return r2


"""
Almost the same as house robber 1, with the exception that we need to cover the fact that 
our house array is actually a big circle, so the last house and first house are not able to be 
robbed together

This could be solved a few ways, but one very simple way included here is to just run the 
hr1 algorithm on the subset of [start --> end - 1] and [start + 1 --> end] in order to get
the two possibilities either including or excluding the end value, and then just take 
the max accordingly. 

"""