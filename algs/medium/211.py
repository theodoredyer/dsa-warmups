class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord
        return dfs(0, self.root)


"""
Fairly tricky Trie problem. 

Setup is very similar to a basic trie, except for the fact that whenever we encounter
a wildcard character, we have to then implement recursive backtracking on all of the 
possible children from that specific point in the string. 

After identifying this the problem isnt too bad and is workable, just pay attention 
to return points and logic flow. 

"""