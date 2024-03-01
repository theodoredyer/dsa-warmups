class Solution:
    def countDigits(self, num: int) -> int:
        snum = str(num)
        count = 0

        unique_digits = []

        for letter in snum:
            unique_digits.append(int(letter))

        for digit in unique_digits:
            if (num % digit == 0):
                count += 1

        return count
        