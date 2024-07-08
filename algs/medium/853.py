class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        pairs.sort(reverse=True)

        stack = []

        for p, s in pairs:

            arrival_time = ((target - p) / s)
            if not stack:
                stack.append(arrival_time)
                continue
            if stack[-1] < arrival_time:
                stack.append(arrival_time)
        return len(stack)
                

"""

Sort the cars by position decreasing, because cars furthest along can't get passed

Then, for each car calculate arrival time, and if a car's arrival time is less than or equal to 
the current stack top's arrival time, we dont need to add another element to the stack, because this
would simply combine into the same fleet, but instead if we have an arrival time AFTER the current stack top's
arrival time, then we should add another element on top of the stack, which will serve as the new fleet 

"""