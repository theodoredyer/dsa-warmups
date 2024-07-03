class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            if not stack:
                stack.append((temperatures[i], i))
                continue


            top_of_stack_temp = stack[-1][0]
            if temperatures[i] > top_of_stack_temp:
                popping = True
                while popping:
                    popped_temp, popped_idx = stack.pop()
                    res[popped_idx] = i - popped_idx
                    if stack and stack[-1][0] < temperatures[i]:
                        continue
                    popping = False
            stack.append([temperatures[i], i])
        return res

                    


            


            
"""
res sets up our return array, when we encounter information needed to populate the number 
of days for a specific temperature we apply that to the res list. 

stack will store temperatures, as well as indices so when we are popping through the stack
we know which result indices to modify

Iterate through all temperatures, if our stack is empty then add temp to stack
if the stack is non empty and the top of the stack (lowest observed current temperature)
is less than our current value, then we know that our current value is the first day since 
the top of the stack with a warmer temperature than the top of the stack, so we take the 
difference in indices from current - top of stack and add that to the result list for the 
start index. 

if our current value is less than the top of the stack then we know for the existing values
we still have not found a day warmer. once we find a day warmer we loop and pop existing values


"""