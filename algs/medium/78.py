class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # part 1 - include idx
            subset.append(nums[idx])
            dfs(idx+1)

            # part 2 - exclude idx
            subset.pop()
            dfs(idx+1)

        dfs(0)
        return res


"""
Utilizes backtracking - at each index we have the option to either add the current element, or not add the current element. 
Becuase we traverse in one direction and the input does not contain duplicate elements, we will never attempt to add a duplicate
to our subset list. 

We have to use copy() to effectively freeze the subset in time, if we don't want future edits to pop from that subset etc. we need to use copy
in order to save the exact state of the subset array at that time, considering it can change. 


Not really finding this one to be super intuitive, revisit later. 
"""