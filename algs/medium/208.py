class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if len(curr.children) == 0:
            return curr.endOfWord
        return True
        


"""
Underlying structure of Tries here is a nested dictionary, where each node exists to store its children,
along with the fact of whether or not that specific node is itself the end of any words in the input set

Nothing really of note here for complexity, other than just remember how to implement this.
Pay attention to edge cases with startsWith, if we traverse to the end of the tree and have no children, but 
current itself is an end of word, that is a valid startswith. 

"""