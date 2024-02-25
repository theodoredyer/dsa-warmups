class Solution:
    def is_palindromic(self, string: str) -> bool:
        return string == string[::-1]

    def isStrictlyPalindromic(self, n: int) -> bool:
        n_str = str(n)

        if len(n_str) == 1:
            return False

        for base in range(2, n - 1):
            n_base_str = ""
            quotient = n
            while quotient:
                quotient, remainder = divmod(quotient, base)
                n_base_str += str(remainder)

            if not self.is_palindromic(n_base_str):
                return False

        return True
