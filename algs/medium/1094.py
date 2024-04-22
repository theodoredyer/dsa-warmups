class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])

        minheap = []
        curpas = 0

        for t in trips:
            npas, start, end = t

            while minheap and minheap[0][0] <= start:
                curpas -= minheap[0][1]
                heapq.heappop(minheap)
            
            curpas += npas
            if curpas > capacity:
                return False

            heapq.heappush(minheap, [end, npas])
        
        return True