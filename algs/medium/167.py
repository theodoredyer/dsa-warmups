class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr = 0
        rptr = len(numbers) - 1

        while lptr < rptr:
            lnum = numbers[lptr]
            rnum = numbers[rptr]
            cursum = lnum + rnum

            if cursum == target:
                return [(lptr + 1), (rptr + 1)]
            elif cursum < target:
                lptr += 1
                continue
            else:
                rptr -= 1
                continue