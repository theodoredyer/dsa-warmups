class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = 0

        for jewel in jewels:
            jewel_count += stones.count(jewel)

        return jewel_count
        