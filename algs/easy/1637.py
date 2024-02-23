class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xpositions = []
        
        for i in range(len(points)):
            xpositions.append(points[i][0])
        
        xpositions = sorted(xpositions)

        biggest_gap = 0

        for i in range(len(xpositions) - 1):
            gap = xpositions[i+1] - xpositions[i]

            if gap > biggest_gap:
                biggest_gap = gap

        return biggest_gap
        