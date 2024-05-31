class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tail_ptr = len(digits) - 1
        carrying_over = False

        while tail_ptr >= 0:
            cur_digit = digits[tail_ptr]

            # Tail case
            if(tail_ptr == len(digits) - 1):
                cur_digit += 1
            # Other cases
            if(carrying_over):
                cur_digit += 1

            if cur_digit == 10:
                digits[tail_ptr] = 0
                carrying_over = True
            else:
                digits[tail_ptr] = cur_digit
                carrying_over = False
            
            if tail_ptr == 0 and cur_digit == 10:
                digits[0] = 1
                digits.append(0)
            
            tail_ptr -= 1

        return digits



"""
Simple problem, my solution might be a little overly verbose because I'm doing this late at night just to get a daily problem done,
but the only thing to really keep in mind here is watch edge cases and be careful to reset variables etc for each iteration and make
sure we're considering the right values. 
"""