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