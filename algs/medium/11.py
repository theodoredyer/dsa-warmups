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
            

"""
The important pattern to recognize, is that when looking at two pointers 
L and R that define the boundary, the area currently created by the two edge boundaries
will be the absolute max area that the smaller of the two boundaries could possibly ever contain

Suppose we have a really low left edge and a really high right edge, regardless of whether or not 
the right edge one index closer to the middle gets even higher, we're just hard stuck because the left 
edge is bad. Thus the only possible increase in area we can observe is when the left edge moves. 

So noting this, just do standard two pointer and do running update checks for a max sum and just 
move the smaller of the two edges 

"""