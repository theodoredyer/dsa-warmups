class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_pos = 0
        max_elevation = 0

        for i in range(len(gain)):
            cur_pos += gain[i]
            if cur_pos > max_elevation:
                max_elevation = cur_pos
        
        return max_elevation
