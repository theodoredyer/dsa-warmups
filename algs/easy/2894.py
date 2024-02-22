class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        counter = 0

        for i in range(1,n+1):
            if i % m == 0:
                counter -= i
            else:
                counter += i
        
        return counter
        