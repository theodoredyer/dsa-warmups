class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        retarr = []

        for i in range(n):
            retarr.append(nums[i])
            retarr.append(nums[i+n])

        return retarr     