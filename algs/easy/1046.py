class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negstones = [-s for s in stones]

        heapq.heapify(negstones)

        while negstones and len(negstones) > 1:
            x = heapq.heappop(negstones)
            y = heapq.heappop(negstones)

            if x < y:
                heapq.heappush(negstones, x-y)
            
        if negstones:
            return heapq.heappop(negstones) * -1
        else:
            return 0


"""
Simple maxheap problem

We want to at any point be able to pull the 2 heaviest stones from a collection
where the weights of stones are going to be updating, this just screams out max heap. 

The only real trick to this is remembering again, python heap syntax and making sure we are 
diligent with tracking what we're doing with our negatives as we need to set this up as a 
negative minheap basically. 

Just iterate while we still have more than 1 stone: 
grab 2 biggest stones by heap popping, then if the stones didn't break
eachother we just add the next stone back onto the heap

Repeat until 1 or 0 remain. 

"""