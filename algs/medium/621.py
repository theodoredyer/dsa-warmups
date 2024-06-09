class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curtime = 0
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()

        while q or maxHeap:
            curtime += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    q.append([count, curtime + n])
            
            if q and q[0][1] == curtime:
                item = q.popleft()
                heapq.heappush(maxHeap, item[0])

        return curtime



"""
Task scheduling heap/priority queue problem:

The only real difficulty from this problem is figuring out how to model the 
problem via maxHeap, and identifying that this is what we need to do. 

Because at any given time we are only intrested in popping the most frequently occurring
element (because we need to space these out with delays) we need to keep track
of the most frequently occurring element, and always select this one. 

one little trick that makes this problem easier (because we don't actually care what the 
sequence is, we only care about the time) is that when we are processing an element and 
associated count, we need to append to the queue only the actual count of this element, because
for the sake of calculating total time we don't care that there are 2 more As in the queue, we only 
care that there are 2 elements in the queue and we need to wait 2 units to process this item any further

so the process is as follows:

- create a counter of each element
- create a maxheap based on these counts
- create a queue that is going to store the remaining number of an element to process
    along with the time that it is going to be able to be processed again

- iterate while we have either a heap, or a queue
for unit of time:
    - process an item from maxheap if it exists, if it does and the remaining count after
        processing this item is not 0, add it to the queue to be added back to heap later
    - check the queue to see if any items are able to be added back into the pool at this timestamp

"""