class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rcount = 0
        lcount = 0
        builder = ""
        substrs = []

        for letter in s:
            if(letter == "R"):
                rcount += 1
                builder += "R"
            else:
                lcount += 1
                builder += "L"

            if rcount == lcount:
                substrs.append(builder)
                builder = ""
                rcount = 0
                lcount = 0

        return len(substrs)
