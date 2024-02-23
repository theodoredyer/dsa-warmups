class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = []

        for account in accounts:
            sums.append(sum(account))

        return max(sums)