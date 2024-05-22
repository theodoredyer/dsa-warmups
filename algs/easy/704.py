class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2
            mval = nums[m]

            if mval == target:
                return m
            elif mval > target:
                r = m - 1
            else:
                l = m + 1

        return -1
