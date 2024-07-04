class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_rep = Counter(p)
        res = []

        if len(s) < len(p):
            return []

        builder_rep = {}

        r = 0
        l = 0

        while r < len(p):
            if s[r] in builder_rep:
                builder_rep[s[r]] += 1
            else:
                builder_rep[s[r]] = 1
            r += 1
        
        r = len(p) - 1
            
        while r < len(s):
            if builder_rep == p_rep:
                res.append(l)

            r += 1
            if r < len(s):
                if s[r] in builder_rep:
                    builder_rep[s[r]] += 1
                else:
                    builder_rep[s[r]] = 1
                if s[l] in builder_rep:
                    if builder_rep[s[l]] == 1:
                        del builder_rep[s[l]]
                    else:
                        builder_rep[s[l]] -= 1
            l += 1
        
        return res





"""
Standard sliding window question, set up dictionary representations of each of the strings, and then with a sliding
iterate through the string checking if our sliding window dict is equivalent to the substring, if so add the left
pointer of this window to result, and then prep window for the next iteration. 


"""