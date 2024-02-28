class Solution:
    def minimumSum(self, num: int) -> int:
        
        nums = []

        for char in str(num):
            nums.append(char)

        nums = sorted(nums)

        num1 = nums[0]
        num2 = nums[1]
        num1 += nums[2]
        num2 += nums[3]

        num1 = int(num1)
        num2 = int(num2)

        return num1 + num2

