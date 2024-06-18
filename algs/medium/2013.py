class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pts = []

        

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) in self.points:
            self.points[(point[0], point[1])] += 1
        else:
            self.points[(point[0], point[1])] = 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:

        res = 0

        px, py = point
        for x,y in self.pts:
            if(abs(py-y) != abs(px-x)) or x == px or y == py:
                continue
            res += self.points[(x,py)] * self.points[(px,y)]
        return res

        
        
