class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            window_len = r - l + 1
            count[s[r]] = 1 + count.get(s[r], 0)

            while max(count.values()) + k < window_len:
                count[s[l]] -= 1
                l += 1
                window_len -= 1
            
            longest = max(longest, window_len)
        return longest


"""
This problem is a little bit tricky in terms of identifying the algorithm, but implementation is fairly straightforward.
The idea we want to leverage, is creating a sliding window to parse through the whole string to achieve O(n) time complexity, and while scanning we want to
keep track of the counts of characters. If a single character (the most frequent one) has occurrances equal to the window length - k (the grace offset) then
we know the existing string is valid, and we can continue to scan right. If we do not meet that criteria, scanning right won't work because our string is invalid
so we need to instead move up our left pointer and then continue scanning forward.

Slight optimization can be made to now have to get the max of the count dictionary by instead just tracking the overall frequency max count, because if we 
dont ever meet a string that is longer than the existing longest, the max count will never be exceeded anbd corresponding longest var wont either. 
"""