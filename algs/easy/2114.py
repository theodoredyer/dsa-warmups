class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maxlen = 0

        for sentence in sentences:
            maxlen =  max(len(sentence.split(" ")), maxlen)

        return maxlen