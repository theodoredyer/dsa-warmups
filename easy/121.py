class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Base case
        if(len(prices) == 1):
            return 0
        
        left_pointer = 0
        right_pointer = 1
        max_profit = prices[right_pointer] - prices[left_pointer]


        while(right_pointer < len(prices)):
            left_val = prices[left_pointer]
            right_val = prices[right_pointer]

            max_profit = max(max_profit, (right_val - left_val))

            if(right_val < left_val):
                left_pointer = right_pointer
                right_pointer += 1
            else:
                right_pointer += 1

        return max(max_profit, 0)
            