class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp


"""
the intuition here is that whenever we reach a new power of 2, we know the binary representation of that contains 1
digit of 1 for the new power of 2, and the rest should be 0s. Following that (next power of 2 + 1) the number of 1s is just
1 (for the current power of 2) + whatever the number of 1s was at n-(power of 2) 

"""