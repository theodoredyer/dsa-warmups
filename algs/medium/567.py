class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring_rep = {}
        for char in s1:
            if char not in substring_rep:
                substring_rep[char] = 1
            else:
                substring_rep[char] += 1
        
        builder_substring = {}
 
        l = 0

        for r in range(len(s2)):
            char = s2[r]
            if r < len(s1):
                if char not in builder_substring:
                    builder_substring[char] = 1
                else:
                    builder_substring[char] += 1
                if builder_substring == substring_rep:
                    return True
                continue
            
            char_to_remove = s2[l]
            if builder_substring[char_to_remove] == 1:
                del builder_substring[char_to_remove]
            else:
                builder_substring[char_to_remove] -= 1
            l += 1
            
            if char in builder_substring:
                builder_substring[char] += 1
            else:
                builder_substring[char] = 1

            if builder_substring == substring_rep:
                return True

        return False
    

"""
At a high level, what we want to do here is first set up a representation of what the 
string s1 looks like as a counter dictionary (occurrances of each value) and then 
via a sliding window approach where we maintain a second dictionary based on a sliding
window of looking through s2 (with window length of s1) we want to see if our dictionary
representation of s1 is ever equivalent to this second builder dictionary

if it is equivalent, we found the substring permutation. If it is not, move the window right by 
incrementing l and removing an instance of the char at l from our builder dict, and then 
incrementing r. 


"""