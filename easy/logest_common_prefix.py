class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        prefix_broken = False

        if len(strs) == 0 or len(strs[0]) == 0:
            return longest_prefix

        prefix_char = strs[0][0]
        idx_track = 0
        while not prefix_broken:
            for elem in strs:
                idx_to_check = min(idx_track, len(elem) - 1)
                if elem[idx_to_check] != prefix_char:
                    prefix_broken = True
                    return longest_prefix
            longest_prefix += prefix_char
            if idx_track + 1 >= len(strs[0]):
                return longest_prefix
            prefix_char = strs[0][idx_track + 1]
            idx_track += 1
