class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            palindromes += self.count_palis(s, i, i)
            palindromes += self.count_palis(s, i, i+1)
        return palindromes
        
    def count_palis(self, s, l, r):
        num_pals = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            num_pals += 1
            l -= 1
            r += 1
        return num_pals

"""
Naive approach is to generate all of the substrings and then check if each are palindromes,
this would require n^2 to generate the substrings and another n to check, so n^3 total. 

instead of this, we're going to just instead for each index try to create palindromes as 
we go so we're doing the generating and checking at the same time effectively, we do this 
by starting pointers at one location and continuing to space them out by one index each 
iteration while comparing the values at these new indices. 

Doing this we leverage only processing new palindromes and achieve n^2

"""