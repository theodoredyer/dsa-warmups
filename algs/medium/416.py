class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsum = sum(nums)

        if numsum % 2:
            return False

        
        dpset = set()
        dpset.add(0)

        tar = numsum / 2

        for i in range(len(nums)):
            nextdp = set()
            for n in dpset:
                potential = nums[i] + n
                if potential == tar:
                    return True
                nextdp.add(potential)
                nextdp.add(n)
            dpset = nextdp
        return False

"""
Dynamic programming

Starting from the end of the list, we want to create a set of the potential sums of subsets
that we've seen so far, we do this by adding the value at each index to every other element 
in our subset (also including 0 to get the value by itself) and seeing if at any point
any of these iterative additions equal our target value (which is half of the sum of the whole array)

Important observations:
- target = sum / 2 because we need subsets that add up to sum and are equal
- start the dpset with 0 to be able to get new numbers by themselves

"""