class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_seen = float("inf")

        while l <= r:
            m = (l+r) // 2

            mval = nums[m]
            lval = nums[l]
            rval = nums[r]

            min_seen = min(min_seen, mval)

            if lval < rval:
                min_seen = min(min_seen, lval)

            if mval >= lval:
                l = m+1
            else:
                r = m-1

        return min_seen



# This problems asks us to run a search on an input array that was sorted, and we need to run the search in log(n) time. This screams binary search
# the caveat being that the array could be rotated just boils down to one decision we need to make - if our left pointer and right pointer are in increasing
# order then we know the segment we're looking at is in sorted order, if they're not then we know the segment we are considering is not in sorted order. If we 
# are known to be in sorted order then we check and see if our left poitner is the min, if not then we have likely already encoutered it earlier on. To determine
# which section of the array we need to investigate, we need to determine if we're in the left sorted or right sorted portion. If our mid pointer is greater
# than or equal to our left pointer, that means we are in the left sorted portion of the array, and the potential min is either already at our l pointer (if 
# the l < r check above went through, then we get the answer updated) and if l > r, then we know iterating on m --> r is going to hold our true min.