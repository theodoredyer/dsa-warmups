class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0

        for idx, num in enumerate(nums):
            if bin(idx).count("1") == k:
                ans += num
        
        return ans