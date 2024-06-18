class Solution:
    def reverse(self, x: int) -> int:
        minv = -2147483648
        maxv = 2147483647

        res = 0

        while x:
            digit = int(math.fmod(x,10))
            x = int(x / 10)

            if (res > (maxv // 10) or (res == maxv // 10 and digit > maxv % 10)):
                return 0
            elif (res < (minv // 10) or (res == minv // 10 and digit < minv % 10)):
                return 0
            
            res = (res * 10) + digit

        return res



"""
To reverse an integer, we want to just applying the following logic:

original number % 10 = first digit

result = that digit

original number /= 10 (so the next modulo gives us the next digit)

next_digit = original_number % 10 again

result = result * 10 to shift left
result = result + next digit

beyond this logic the rest of the problem is just conditional checks. 

"""