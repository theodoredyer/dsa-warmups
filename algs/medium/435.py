class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num_removed = 0
        intervals.sort(key=lambda i: i[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] <= intervals[i+1][0]:
                continue
            else:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i+1] = intervals[i]
                num_removed += 1
        
        return num_removed


"""
Good problem for interval review if I need it later

In order to determine the minimum number of intervals we need to remove, as 
with most interval problems in order to get information about contrasting
intervals we want to sort by the start value of each interval

The tricky part of this problem to identify is that we need a greedy solution

When we come to identify that we are at an index where we have a collision between
index i and index i+1, the interval we should delete should just be whatever
the interval with the smaller end index is, because this will minimize the number 
of future collisions with other intervals. 

So we want to loop through the array until we find a collision point, when we do
we need to increment the number of minimum collisions, and then just somehow
remove the larger of those two overlapping intervals from future consideration, 
I chose to do this by overwriting the value in the intervals array for the next
iteration to just be the smaller interval

where 'smaller' interval means within the collision, the one with a smaller
end value. 

"""