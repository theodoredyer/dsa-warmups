class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(str_a, str_b):
            opt_a = str_a + str_b
            opt_b = str_b + str_a

            if opt_a > opt_b:
                return -1
            else:
                return 1
        

        for i, n in enumerate(nums):
            nums[i] = str(n)

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))
        
    