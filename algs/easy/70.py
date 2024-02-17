class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [] * n
        dp[n] = 1
        dp[n-1] = 1

        for i in range(n-2, 0):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0]