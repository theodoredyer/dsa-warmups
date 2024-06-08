class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[::])
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
            


    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


"""
Backtracking problem, with a slightly type of data to track rather than
a standard subset of an original array, etc. 

For index, we want to determine for the remaining part of the string how we can
divvy it up into different substrings that are palindromes, we do this by the following:

if our current index we're looking at is past len(input), then we know the current
partition set we've been building up is valid, so we should add a copy of our partition 
set to the result, and then return and try a different partition set. 

We are going to start by looking from current index to the end of the string, and 
seeing if we can create any substrings that are palindromes by using our helper function, then
proceed to dfs into the remaining substring to see if we can generate more valid palindromes
to reach the end of the string, if not we are going to just return back to the next
call and all is well.

Need to make sure we are managing our current partition properly - and we do this 
by whenever we find a new valid substring, add it to partition, but then after we call
dfs on the remaining portion, need to make sure we remove that last substring from partition.


Helper function is_palindrome
- basic function to determine whether or not a subset of a string from index 
l to index r is a palindrome
"""