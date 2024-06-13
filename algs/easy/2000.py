class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        ch_idx = 0

        for i in range(len(word)):
            if word[i] == ch:
                ch_idx = i
                break

        sub = word[:ch_idx+1]
        rest = word[ch_idx+1:]

        return sub[::-1] + rest
    

