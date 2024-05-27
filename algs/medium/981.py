class TimeMap:

    def __init__(self):
        self.store = {} #  key is str, val is list of lists (pairs) (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        value_list = self.store.get(key, [])

        # bin search
        l, r, = 0, len(value_list) - 1

        while l <= r:
            m = (l+r) // 2

            midval = value_list[m][1]
            if midval <= timestamp:
                res = value_list[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


"""
Relatively straightforward, just setting up a class that supports a time based key value store, the idea is simple to set up a dict, where the keys map
as appropriate, and then to accomplish the time based aspect just append values to a list of lists for that specific key, where we are storing the value 
and timestamp. 

this problem has an important constraint to note, which is that values are inserted in order of increasing time, so we know they will be sorted according 
to timestamp, and thus we can binary search for the get command because it is sorted. 

"""