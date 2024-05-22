class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        water = 0

        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                water += max(0, maxL - height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += max(0, maxR - height[r])
        
        return water