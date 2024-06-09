class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        

"""
Standard heap problem

In this case where we want to keep track of the k largest (to find the kth largest) 
elements, the idea is to use a minheap, as a way of filtering out the minimums. 

If suppose we encounter n elements, and we pop off the minimums until we have k elements,
we have the k largest elements, and we then encounter another element that is larger, after
just doing one more pop, the k largest minheap will be preserved

Although its not intuitively obvious, minheaps let us track the k largest elements because
they allow us to find and remove the smallest (minimums) in constant time. 

After recognizing this, the problem just comes down to knowing python heap syntax

plainlist = [1, 2, 3]

heap = heapq.heapify(plainlist, )

"""