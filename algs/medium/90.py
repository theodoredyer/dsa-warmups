class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # Recurse for subsets including i
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # Recurse for subsets not including i
            while (i + 1 < len(nums)) and (nums[i] == nums[i+1]):
                i += 1
            backtrack(i+1, subset)
        backtrack(0, [])
        return res


"""
Standard backtracking solution, need to first start by sorting the input array to 
help later on with a duplicate handling trick, and then set up recursive function:
at each index, we want to generate all of the possible subsets that include nums[index]
and then proceed to generate all of the possible subsets that don't include nums[i]. One 
caveat to note, is that to make sure we are not hitting duplicates, when we decide to recurse
for all of the subsets that don't include nums[index] we actually have to continue to 
increment our i pointer to point to whatever the next non nums[index] value is, so for example:

[1, 2, 2, 3]

Running all of the case 1 recursive calls will capture all of the values including [1, 2, 2] but
when we want to do the case where we don't include the first 2, we need to actually swap to cases where 
we dont include any of the 2s. 

Apart from this we follow standard backtracking of:

def recurse(index, current subset)
    if current index is end of array:
        append subset and return
    
    recurse for subsets including nums[i]
    recurse for subsets not including any instance of nums[i]

Potential number of subsets is 2^n, and the length of each subset is at worst n, so
our overall time complexity here is n2^n
"""
