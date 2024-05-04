class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for lptr in range(len(s) - 9):
            cur = s[lptr:lptr+10]

            if cur in seen:
                res.add(cur)

            seen.add(cur)

        return list(res)