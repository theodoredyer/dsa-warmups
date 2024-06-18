class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        result = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):

                digit = int(num1[i1]) * int(num2[i2])

                result[i1+i2] += digit
                result[i1+i2+1] += (result[i1+i2] // 10)
                result[i1+i2] = result[i1+i2] % 10

        result = result[::-1]

        k = 0
        while k < len(result):
            if result[k] == 0:
                k += 1
            else:
                break
        result = map(str, result[k:])
        return "".join(result)



"""
Only really important thing to note is that multiplying item at index i in num1 and index k in num2
just means adding the result digit to index i+k in the result. 

Beyond that for this problem we just need to handle the overflow cases etc. But that is all

"""