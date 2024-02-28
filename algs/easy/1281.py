class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strnum = str(n)

        sum_digs = 0
        prod_digs = 1

        for ch in strnum:
            intchar = int(ch)

            sum_digs += intchar
            prod_digs *= intchar

        return prod_digs - sum_digs