class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = sorted(nums)
        retarr = []

        for num in nums:
            count = 0
            for snum in snums:
                if num > snum:
                    count += 1
            retarr.append(count)

        return retarr
                    