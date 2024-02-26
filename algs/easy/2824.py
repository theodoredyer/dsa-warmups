class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        pairs = 0

        snums = sorted(nums)

        for i in range(len(nums) - 1):
            k = i + 1
            while k < len(nums):
                if snums[i] + snums[k] < target:
                    pairs += 1
                k += 1

        return pairs

