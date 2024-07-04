class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        goal_sum = total_sum // k
        
        subarrs = [0] * k
        nums.sort(reverse=True)
        
        def backtrack(index):
            if index == len(nums):
                return True
            
            for i in range(k):
                if subarrs[i] + nums[index] <= goal_sum:
                    subarrs[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    subarrs[i] -= nums[index]
                
                # Optimization: If subarrs[i] is 0, further subsets will also be 0, skip them
                if subarrs[i] == 0:
                    break
            
            return False
        
        return backtrack(0)


"""
Backtracking - very similar to matchsticks problem

the idea is that we want to create all of the possible permutations of subsets k
under the condition that each subset must achieve the exact sum that evenly divides
the overall set. 

Note - do not do something like :

for subarr in subarrs: because here we're working directly with the internal ints/references
and things aren't tracking properly, instead we want to just work directly with 

for i in range(len(subarrs)):
subarr[i]

because here we're actually mofifying subarrs (the list) not the ints. 

"""