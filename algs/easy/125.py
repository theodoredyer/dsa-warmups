class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True  # Empty string is considered a valid palindrome

        lptr = 0
        rptr = len(s) - 1

        while lptr < rptr:
            while lptr < rptr and not s[lptr].isalnum():
                lptr += 1
            while lptr < rptr and not s[rptr].isalnum():
                rptr -= 1

            if s[lptr].lower() != s[rptr].lower():
                return False
            else:
                lptr += 1
                rptr -= 1
        return True
