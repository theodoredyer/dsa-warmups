class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num_unique = 2 ** k

        seenset = set()

        for char in range(len(s) - k + 1):
            current_substr = s[char:char+k]

            seenset.add(current_substr)

        return num_unique == len(seenset)