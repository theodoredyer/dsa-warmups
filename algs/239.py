class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        if len(nums) < k:
            return 

        l = 0
        r = 0

        q = collections.deque()

        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res



"""
The idea here is to keep track of our current max via a monotonically decreasing queue

The intuition behind this is that when we encounter new elements we want to be able t
to add them to the top of the queue, in case we don't see any larger elements for k more steps
then this element will be the largest element in the q and used later on, however as soon as
we encounter a larger element, that element is going to be used as the max for all of the 
future steps that anything in the q currently could have been used for, so get rid of everything. 

remove the back of the queue only when it falls out of consideration range aka the index of that 
element is < l 

"""