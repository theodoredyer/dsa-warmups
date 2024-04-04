class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        already_altered = False

        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if already_altered:
                return False

            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            
            already_altered = True

        return True
