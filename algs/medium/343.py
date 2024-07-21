class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = {1:1}

        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1,num):
                possible_max = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], possible_max)
            return dp[num]
        
        return dfs(n)
    


"""
Pretty clearly needs to use some sort of recursive solution to calculate all of the possibilities

Set up a DFS with base case of if num == 1, return 1

else we want to calculate the max for a particular num as the max of all possibilities we can create from
that num

so for example the max for 4 is the max of (1,3), (2,2), (3,1)

and we set up these calculations in a for loop making recursive calls to the other nums. 

After doing this we cache the value for num in a dp dictionary so that if we encoutner that same 
number later on we just immediately return it in any recursive calls. 


"""