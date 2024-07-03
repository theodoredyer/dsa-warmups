class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        house_ptr = 0
        heat_ptr = 0
        biggest_gap = 0
        houses.sort()
        heaters.sort()

        while house_ptr < len(houses):
            while heat_ptr < len(heaters) - 1 and abs(houses[house_ptr] - heaters[heat_ptr]) >= abs(houses[house_ptr] - heaters[heat_ptr + 1]):
                        heat_ptr += 1

            current_gap = abs(houses[house_ptr] - heaters[heat_ptr])
            biggest_gap = max(biggest_gap, current_gap)
            house_ptr += 1
        
        return biggest_gap


"""
Fun problem - could be slightly optimized with binary search.. 

It initially sounds like a greedy algorithm type problem but the approach looks 
more like standard two pointer, basically we need to start by sorting both the 
houses and the heaters

Following this we set up our two pointers, one for houses and one for heaters

for each house, check to see if the next heater is closer, if it is then increment 
our heater pointer and calculate the max distance from each house to the closest 
heater. 

the problem is asking for 'heater radius' which in this problem makes way more sense to 
just instead think about the max distance to the min heater for each house. 

Doing this we just iteratively keep trakcing what this max is and return it. 

"""