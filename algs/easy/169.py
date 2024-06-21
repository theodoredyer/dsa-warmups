class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnts = Counter(nums)

        for c in cnts:
            if cnts[c] > (len(nums)/2):
                return c
