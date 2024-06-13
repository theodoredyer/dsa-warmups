class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        valdict = Counter(hand)

        minheap = list(valdict.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]
            for i in range(first, first + groupSize):
                if i not in valdict:
                    return False
                if valdict[i] == 0:
                    return False
                valdict[i] -= 1
                if valdict[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True



"""
Set up a counter of all of the values we have available to reference back 
to later on, alternative we could do some sorting of a list and tracking external
variables but setting up the counter is probably easier

next, we want to set up a minheap to track the 'state' of the remaining elements
effectively. We want to pull the first element of the minheap, and then proceed to
search for i in range(minheap(min) to minheap(min) + group size). While checking through
we want to see if the remaining count for each number reaches 0, if so we want to pop it

and then one other check is that if we are trying to remove an element from out minheap 
or in other words if the value for the dictioanry at that key reaches 0, we want to check 
to make sure that this element is actually the minimum element of the minheap, if it isn't
then we are creating a gap where we will still have min_element in the minheap 
and a gap from that element to the next element, so basically there's no continuity. and
the future straights are invalid. 

"""