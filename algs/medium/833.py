class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        k = len(indices)
        valid_replacements = []

        for i in range(k):
            if s[indices[i]:(indices[i] + len(sources[i]))] == sources[i]:
                valid_replacements.append((indices[i], sources[i], targets[i]))
        
        valid_replacements.sort(key = lambda x:x[0])
        base_s_pointer = 0
        res = []

        for start, source, target in valid_replacements:
            res.append(s[base_s_pointer:start])
            res.append(target)
            base_s_pointer = start + len(source)
        
        res.append(s[base_s_pointer:])

        return "".join(res)

"""
Determine which replacements are valid via a first pass through the array
(in order for us to be able to check if a replacement is valid we need reference
to the original array, or do really tricky pointer tracking)

After finding valid replacements, sort them by increasing index. 

Starting from the base of the original string, for each valid replacement
we want to add the source string from the base --> the start index of the replacement
after this, we add the replacement, and then set the base pointer to be where the 
pointer would be at the end of the old source string ie start index + len(source)

after processing each valid replacment, add the rest of the base string and return 


"""