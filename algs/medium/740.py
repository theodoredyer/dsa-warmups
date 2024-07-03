class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        charcounts = Counter(nums)
        
        snums = sorted(list(set(nums)))
        dp = [0] * len(snums)
        dp[0] = charcounts[snums[0]] * snums[0]

        for i in range(1, len(snums)):
            if snums[i] - 1 > snums[i-1]:
                dp[i] = dp[i-1] + (charcounts[snums[i]] * snums[i])
            else:
                if i < 2:
                    dp[i] = max((charcounts[snums[i]] * snums[i]), dp[i-1])
                else:
                    dp[i] = max((charcounts[snums[i]] * snums[i]) + dp[i-2], dp[i-1])

        
        return dp[len(snums)-1]
        


"""

Very similar to the house robber problem for dynamic programming

The idea here is that we want to keep a running track of for each index what 
the maximum score is we can reach for that index by abiding by certain underlying rules

First we need to do some setup, that being that whenever we 'pick' a value, the score
we earn from that is actually value * occurrances, so set that up in a counter hash map

Next, we want to sort the remaining numbers and remove duplicates so we can just cleanly 
apply the following logic while moving through:

the max for a current index is either the previous index's max + the current value's
potential score if the current value is > last value by more than 1, or if we do have a 
collision and can't collect both values, then we take the max of the current index + max of two 
indices back, or the previous index. 


"""