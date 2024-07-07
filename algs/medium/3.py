class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        trackset = set()
        longest = 0

        lp = 0

        for rp in range(len(s)):

            while s[rp] in trackset:
                trackset.remove(s[lp])
                lp += 1

            trackset.add(s[rp])

            longest = max(len(trackset), longest)

        return longest

            
"""
Maintain sliding window, when incrementing r see if new value is already in our set
and if it is, increment l until it isn't

Track and update maxes along the way. 

"""