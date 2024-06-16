class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for i in range(len(s)+1)]
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            substr = s[i:]
            for word in wordDict:
                if (i+len(word) <= len(s)) and word == substr[:len(word)]:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        
        return dp[0]

"""
Standard dp problem

Logic is to work from the back of the array to the front, and keep track of a list of 
boolean values where the value at an index refers to whether or not we can reach the end of 
the list from that index (if for a substring we can parse the rest of the list with words
in our dictionary). 

Setting this up to contain False for all values and True for the last value, we then iterate
through the list backwards until we find a substring that contains a word in our dictioanary
or multiple words in our dictionary. 

We then (for each word) see if we can apply that word to arrive at a True value in the DP subarray
which would indicate we can successfully break the word down from this point if we use that word. 
if a specific word doesn't arrive at a true value, we try all of the other words before moving on

If we instead worked front to back it would be much harder to neatly apply all of the possibilities. 

"""