class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda i: i[0])
        res = []

        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            while i < len(intervals) - 1:
                if end >= intervals[i+1][0]:
                    end = max(end, intervals[i+1][1])
                    i += 1
                else:
                    break
            res.append([start, end])
            i += 1

        return res



"""
DON'T OVERTHINK IT

this problem only becomes complicated if we overcomplicate things with extra variables
and things. 

It is intuitive here that when we are figuring out if we need to merge intervals
we should start first by sorting the intervals by the start index of each interval

Then follow this logic:

for each interval:
    start = interval[0]
    end = interval[1]

    (if we are not at end of the list)
        (if interval[i+1] start value is less than or equal to our end)
            new end = max of current end, and next interval's end.
            increment i
        (else)
            break
    insert start/end as new interval
    

"""