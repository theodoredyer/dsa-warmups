class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_pairs = 0
        cur_idx = 0
        for i in range(len(nums)):
            subarr = nums[(i+1):]

            num_pairs += subarr.count(nums[i])

        return num_pairs


        