class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for curamt in range(1, amount + 1):
            for c in coins:
                if curamt - c >= 0:
                    dp[curamt] = min(dp[curamt], 1 + dp[curamt - c])

        return dp[amount] if dp[amount] != (amount + 1) else -1


"""
Standard DP problem:

Starting from the bottom up, where dp[0] means it requires 0 coins to create the amount (0), 
for each amount, we try to subtract each coin's value from that amount. If the result is positive 
or zero, that means this coin is a valid coin that could lead us to our result, so we're going to 
set the minimum coins needed for that specific amount to be the minimum of itself, and 
(1 + dp[amount - coin value]) meaning, if we add the coin c, the result will be 1 coin + the dp 
of the remainder value. 

After we iterate through all of the different coins, this will result in us continuing to set our min to whatever the 
combination of coins is that actually brings us to our min. 

"""