class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)
        if "-" in strnum:
            return False

        revstr = "".join(reversed(strnum))

        for i in range(len(strnum)):
            if strnum[i] != revstr[i]:
                return False

        return True

        