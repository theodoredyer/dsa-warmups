class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, a in enumerate(nums):

            if idx > 0 and a == nums[idx-1]:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    
        return res

"""
Recognize that sorting is acceptable and correct here

After sorting, our a value is the lowest value in the array and b and c can be any of the
remaining values. 

If we encounter a duplicate a value on the next iteration just continue because 
we know any b and cs that satisfy this a value will just cause dupes. 

"""