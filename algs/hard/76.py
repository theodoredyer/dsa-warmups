class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        srep = defaultdict(lambda: [0,0])

        for c in t:
            srep[c][1] += 1

        required = len(t)
        min_len = float('inf')
        min_start=0
        l = 0

        for r in range(len(s)):
            rchar = s[r]

            if rchar in srep:
                if srep[rchar][0] < srep[rchar][1]:
                    required -= 1
                srep[rchar][0] += 1

            while required == 0:
                if (r-l +1) < min_len:
                    min_len = r-l+1
                    min_start = l
                if s[l] in srep:
                    srep[s[l]][0] -= 1
                    if srep[s[l]][0] < srep[s[l]][1]:
                        required += 1
                l += 1
        if min_len == float('inf'):
            return ""
        return s[min_start:(min_start + min_len)]
            
"""
Maintain a dictionary with keys equal to each letter in our required substring, 
and values of an array containing [x,y]

where x = the occurrances of this character in our current window
and y = the occurrances of this character required for our substring to be valid

sliding through the whole array, with an initial count of required charcters equal to 
the length of t,when we achieve a required character count == 0 after decrementing when we 
find matching characters and add them to the dict, we want to shrink the subarray from the left
as far as we can, tracking maxes along the way. 


"""