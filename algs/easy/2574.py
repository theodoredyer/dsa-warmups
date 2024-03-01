class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightsum, leftsum, final = [], [], []

        numsrev = nums[::-1]

        for i in range(len(nums)):
            if i == 0:
                rightsum.append(0)
                leftsum.append(0)
            else:
                leftsum.append(leftsum[i-1] + nums[i-1])
                rightsum.append(rightsum[i-1] + numsrev[i-1])

        rightsum = rightsum[::-1]

        for i in range(len(nums)):
            final.append(abs(leftsum[i] - rightsum[i]))

        return final