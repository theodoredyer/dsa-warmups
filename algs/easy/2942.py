class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        matching_indices = []

        for word in enumerate(words):
            if x in word[1]:
                matching_indices.append(word[0])

        return matching_indices