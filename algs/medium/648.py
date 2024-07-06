class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wordset = set(dictionary)

        def root_replace(word):
            builder_substr = ""

            for i in range(len(word)):
                builder_substr += word[i]
                if builder_substr in wordset:
                    return builder_substr
            return word

        words = sentence.split()
        reswords = [root_replace(word) for word in words]

        res_str = ""
        for word in reswords:
            res_str += (word + " ")
        return res_str[:len(res_str) - 1]




"""
Create a helper function to detect if a incrementing prefix/builder 
substring is inside our set of dictionary words, if it is then immediately
return the current state of the prefix, if it is not then return the whole word. 

After writing this function, just apply this function to all of the words in the 
string and build the string back to what it was. 

"""