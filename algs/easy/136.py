class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for e in nums:
            res = res ^ e

        return res

"""
Intuition is xor with 0 doesn't change the result, and when we xor all of the 
elements that have duplicates, this is going to result in 0s across the board. 

So intuition follows that xor'ing the non duplicate with all 0s is just going to return the
same non duplicate.

"""