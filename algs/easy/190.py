class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            curbit = (n >> i) & 1
            res = res | (curbit << (31-i))
        
        return res


"""
For each index in the digit, the reversed value is equivalent to that digit left shifted 31-i times. 

Using this fact, we can run an iteration where we determine if bit at index i is == 1 by right shifting i times 
and anding the result with 1, and then determining the value this corresponds to by left shifting 31-i times, and then or this 
value into our result value. 

"""