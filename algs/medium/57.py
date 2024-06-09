class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res


"""
In order to determine where we want to insert our new interval, we need to 
iterate through the input list (which is sorted in increasing order) and 
run a couple of checks at each iteration. 

If the end of our new interval comes before the start of the next interval,
we know it is safe to append our new interval, and then the rest of the intervals
list. 

If the start of our interval comes after the end of the next inerval, we know
it is safe to add the next interval and continue the iterative search with our
new interval

if neither of these are true, we know that our newInterval is going to envelop our 
next interval that we're looking at, so set the newInterval to be the envelopment
of the next interval with min/max, and continue looking

Remember to add the base case of appending our newInterval if we never meet 
condition 1.

"""