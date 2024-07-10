class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curlen = r - l + 1

                if curlen > reslen:
                    res = s[l:r+1]
                    reslen = curlen

                l -= 1
                r += 1

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curlen = r - l + 1

                if curlen > reslen:
                    res = s[l:r+1]
                    reslen = curlen

                l -= 1
                r += 1

        return res
    
"""
For each index in the array, start from an empty substring and set up L and R
pointers to look at our starting index, just keep pushing out the l and r pointers until a boundary gets 
hit or we no longer have the same values (to keep the palindrome valid) and then update our
max if the current max is bigger. 

We also have to account for the even length substrings, and we do this by doing a second pass
but instead of setting l and r both to i, we set r to i+1 to start on an offset. 

"""