class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp = {}

        lenLis = 0
        occLis = 0

        for i in range(len(nums) - 1, -1, -1):
            maxlen = 1
            maxcnt = 1

            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    jlen, jcnt = dp[j]
                    if jlen + 1 > maxlen:
                        maxlen = jlen + 1
                        maxcnt = jcnt
                    elif jlen + 1 == maxlen:
                        maxcnt += jcnt

            if maxlen > lenLis:
                lenLis, occLis = maxlen, maxcnt
            elif maxlen == lenLis:
                occLis += maxcnt

            dp[i] = [maxlen, maxcnt]

        return occLis




"""
Tricky DP problem:

Create a hashmap tracking at each index what the length of the max LIS is from that index,
alongside the number of ways we can reach that LIS:
index = [len, count]

Iterating backwards through our array, for each index we want to look towards the end 
of the array and when we encounter a value that is greater than our current value (indicating
that we could start a new longest increasing subsequence) we want to set our current 
LIS length to the max length at the new value + 1, and set our count to be the count 
of the previous value 

for example if we have 

1 3 5 4 7

when getting to 3 we can see that from 3 we have two ways to get LIS of 3
(3/5/7 or 3/4/7) and when we add 1 (which is a smaller value than 3) we equally now
have two ways to reach LIS of 4 by just prepending 1 to each of those two lists ^

If however we do not have a value that is increasing, then we know that from our current value we
do not have any other LISs and our maxlen/maxcnt stays at 1

Lastly, after we process all possibilities for each value at each index, we want to see
if the newly calculated maxLis and maxLiscount are greater than the globals, if they are then 
we want to set the globals accordingly. 

If we find a enw maxlen, our new maxLen should just be the new len, and our maxcount 
should be max count. 

Alternatively if we find an equal length to the current max, then we should add the count
of the current list to the global count. 

"""
