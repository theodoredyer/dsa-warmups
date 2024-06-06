class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum = 0
        char_dict = {}

        for i in range(len(s)):
            snum = s[i]
            tnum = t[i]

            if snum in char_dict:
                char_dict[snum][0] = i
            else:
                char_dict[snum] = [i, 0]
            
            if tnum in char_dict:
                char_dict[tnum][1] = i
            else:
                char_dict[tnum] = [0, i]

        for key in char_dict:
            sum += abs(char_dict[key][0] - char_dict[key][1])

        return sum


"""
Set up dictionary to store the indices of each char in each array
this could be simplified to only use a dictionary of key:int and just build the running sum
and then calculate the abs diff at the end
"""