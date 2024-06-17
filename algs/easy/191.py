class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            res += n % 2
            n = n >> 1
        return res

"""
To determine if a given digit is 1, we can and it with one to see if the result is still 1, or we can mod 2 and see if the result is 1,
because that would mean our first digit is 1 / an odd number. 

After doing this, if we logical right shift the number 1 bit to the right and repeat, we can check every digit to see how many 1s we have
and increment the counter while going through. 

"""