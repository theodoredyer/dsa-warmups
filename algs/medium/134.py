class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0
        valid_start = 0
        diff = []

        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        if sum(diff) < 0:
            return -1

        for k in range(len(gas)):
            
            # Fuel up
            current_gas += diff[k]

            if current_gas < 0:
                current_gas = 0
                valid_start = k+1

        return valid_start
            
            


"""
Standard greedy problem, we first start by setting up a list that contains the difference between the gas
gained at a location, and the expenditure from that location to the next. 

Doing this, we can loop through the array starting at 0 gas, and seeing if the route starting at the current
route causes us to dip below 0 gas at any point, if we dip below 0 then we know the route is not viable. 

whenever we dip below 0, we reset the gas to 0 (as if we selected the new index as our starting point) and
then we try carrying on from the current index (saving what our current index is) if we reach the end of the 
array and our current gas doesn't dip below 0, then we know that the selection of the previous current index
was a valid starting point, and then we return that last current index. 
"""