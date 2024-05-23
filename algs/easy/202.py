class Solution:
    def isHappy(self, n: int) -> bool:
        seen_sums = set()
        curstr = str(n)

        while True:
            tempsum = 0
            for c in curstr:
                tempsum += int(c) * int(c)
            if tempsum in seen_sums:
                return False
            elif tempsum == 1:
                return True
            seen_sums.add(tempsum)
            curstr = str(tempsum)


"""
this is a pretty strightforward problem, in order to determine if a numbeer is non cyclical, we need to just keep track of the sums we have already seen 
to identify if we arrive at a duplicate sum, in which case we want to just return false, in all other cases we would arrive back at 1 and should return true. 
"""
