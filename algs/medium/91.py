class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] not in "789")):
                res += dfs(i+2)
            dp[i] = res
            return res

        return dfs(0)


            

"""
Adding this one to the review set, it doesn't really come naturally to me. 

can be done recursively or with just dp iteratively:

For each index we want to see first off, if it is just "0" then return 0, because by itself this does not work as a number. 

Also, if our index is already cached in dp, then return dp. 

else, our value should be equal to dfs(i+1) + if i+1 could make up a valid double digit string like 19 or something, increment
result by also dfs(i+2)

After running this calculation, add the dp value for i to our running dp hashmap. 

return dfs(0)

"""