class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            if not stack:
                stack.append((n, i))
                continue

            if stack[-1][0] >= n:
                stack.append((n,i))
            else:
                popping = True
                while(popping):
                    smaller_element = stack.pop()
                    prev_index = smaller_element[1]
                    res[prev_index] = i - prev_index
                    if stack and n > stack[-1][0]:
                        continue
                    popping = False
            stack.append((n,i))

        return res


            
