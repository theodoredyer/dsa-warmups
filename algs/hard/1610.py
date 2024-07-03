class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        def getAngle(x,y):
            x -= location[0]
            y -= location[1]
            return (((math.atan2(y,x)/(math.pi))*180)+360)%360

        at_user = 0
        angles = []

        for x, y in points:
            if location[0] == x and location[1] == y:
                at_user += 1

            else:
                angles.append(getAngle(x,y))

        angles.sort()
        angles += [a + 360 for a in angles]

        r, l = 0, 0
        maxvis = 0

        while r < len(points):
            if angles[r] - angles[l] <= angle:
                r += 1
                maxvis = max(maxvis, r-l)
            else:
                l += 1
        return maxvis + at_user

