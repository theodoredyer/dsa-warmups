class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            max_for_i = lis[i]

            for k in range(i+1, len(nums)):

                if nums[i] < nums[k]:
                    max_for_i = max(max_for_i, lis[k] + 1)
                
            lis[i] = max_for_i

        return max(lis)


"""
Dynamic programming:

In order to find the longest increasing subsequence, we start at the end of the array
and set up some logic:

if we are at the end of the array, this subsequence has max length 1. 
if we are not at the end, the maximum of our current position is the maximum
of either 1, or the maximum of any value further along in the array that the 
current value we're looking at is less than + 1 because we're adding on our current value


"""