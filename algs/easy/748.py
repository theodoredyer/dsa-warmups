class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lpc = collections.Counter()

        for c in licensePlate.lower():
            if c.isalpha():
                lpc[c] += 1
        
        shortest = "z"*20

        for word in words:
            wc = collections.Counter(word)

            if(wc & lpc) == lpc:
                if len(word) < len(shortest):
                    shortest = word
        return shortest
        