class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        leng = sum(matchsticks) // 4

        if sum(matchsticks) / 4 != leng:
            return False

        sides = [0] * 4

        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for s in range(len(sides)):
                if sides[s] + matchsticks[i] <= leng:
                    sides[s] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[s] -= matchsticks[i]
            return False
        return backtrack(0)
    

"""

Standard recursive backtracking problem 

We're using backtracking because this problem involves having to compute a bunch of different
permutations to try and find a permutation that works

Logic is as follows:

- Each side has to be equal to the sum of matchsticks / 4 in order for this to be a complete and 
proper square. 

- set up a list of sides that store the current length of that side, and for each matchstick 
in the input array try to add it to each side and recurse until it either breaks and backtracks, 
or successfully processes that side and moves on to the next one. 

Big optimization here is possible by sorting in reverse order to either send the most simple/large
matchsticks first, or to fail quickly if the sticks are too large for each section. 

if we start with the smaller sticks, we are doing more computation. Also the nlogn sort is
inconsequential in the larger picture. 

"""