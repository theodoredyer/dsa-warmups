class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Trivial version, using heap

        nnums = [-n for n in nums]

        heapq.heapify(nnums)

        for i in range(k-1):
            heapq.heappop(nnums)

        return heapq.heappop(nnums) * -1


"""
Trivial when using heaps, to get the kth largest we just create a heap, and 
then proceed to pop k times and return the kth pop element. 

More sophisticated version available with quickselect, but for now ignoring that
"""