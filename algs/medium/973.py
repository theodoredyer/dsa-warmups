class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        origin = [0,0]
        aux_arr = []
        for p in points:
            origin_dist = self.calc_euclid(p, origin)
            aux_arr.append([origin_dist, p])
        
        heapq.heapify(aux_arr)

        ret_list = []

        for i in range(k):
            ret_list.append(heapq.heappop(aux_arr)[1])

        return ret_list


    def calc_euclid(self, p1, p2):
        return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


"""
Basic heap problem, we need to return the top k things is standard heap candidate

The only thing different here is we have to create the heap based on an attribute
that isn't immediately in the input data, we have to create the distance based on 
some distance calcualation and then make the heap based on this distance 

With heapq.heapify, it used by default the first value in a tuple. 
"""