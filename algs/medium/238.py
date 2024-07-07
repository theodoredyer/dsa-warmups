class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)

        # calc prefixes
        i = 1
        while i < len(prefixes):
            prefixes[i] = prefixes[i-1] * nums[i-1]
            i += 1
        print(prefixes)

        # calc postfixes
        i = len(postfixes) - 2
        while i >= 0:
            postfixes[i] = nums[i+1] * postfixes[i+1]
            i -= 1

        return [prefixes[i] * postfixes[i] for i in range(len(nums))]
    

"""
Simple problem just using prefix and postfix multiplication, 

Just remember that the prefixes should look like
i = 1
while i < len(nums):
    prefix[i] = nums[i-1] * prefix[i-1]

and postfix similarly is 
i = len(nums) - 1
while i >= 0:
    postfix[i] = nums[i+1] * postfix[i+1]

At no point in the definition for postfix or prefix of i is the actual 
index of i involved. 

"""