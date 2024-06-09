
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [item.start for item in intervals]
        ends = [item.end for item in intervals]

        starts.sort()
        ends.sort()

        startptr = 0
        endptr = 0

        count, max_count = 0, 0

        while startptr < len(starts):
            if starts[startptr] < ends[endptr]:
                count += 1
                max_count = max(max_count, count)
                startptr += 1
            else:
                count -= 1
                endptr += 1

        
        return max_count


"""

In order to identify how many meeting rooms (or days) basically just some separate
partition to make sure all of the meetings work, we need to actially identify
the maximum number of meetings going on at one time. 

DRAW THIS ONE OUT ON PAPER

In order to solve this, we want to parse all of our meeting start times 
and our meeting end times in increasing timeline order. 

If a meeting starts, concurrent meetings += 1
If a meeting ends, concurrent meetings -= 1

If two meetings have the same timestamp, that does not count as overlap for 
this problem, so we want to process the meeting ending first. 

So in order to get all of these timestamps, we need separate arrays for start
and end times, and just sort them by timestamp and have a pointer for each one. 

"""