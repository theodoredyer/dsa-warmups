class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        lptr = 0
        rptr = len(heights) - 1

        while lptr < rptr:
            hl = heights[lptr]
            hr = heights[rptr]
            distance = rptr - lptr

            max_area = max(max_area, min(hr, hl) * distance)
            
            if hl < hr:
                lptr += 1
            else:
                rptr -= 1

        return max_area
            