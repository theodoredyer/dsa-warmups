class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res

            return x * res if n % 2 else res


        res = helper(x,abs(n))
        return 1/res if n < 0 else res


"""
A bit tricky to identify that this is a divide and conquer recursive question, but essentially we just set up a helper 
recursive function and within this function, if our exponent is greater than 2 we're going to split this into multiplying 
by that exponent twice in two different calls, and handle the edge case of not multiplying an extra time when our 
exponent is odd at the base case. 

"""