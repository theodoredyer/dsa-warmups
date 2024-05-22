class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def simulate_eating(piles, k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours

        l = 1
        r = max(piles)
        minimum_rate = r

        while l <= r:
            m = (l + r) // 2
            hours = simulate_eating(piles, m)
            if hours > h:
                l = m + 1
            elif hours <= h:
                minimum_rate = min(minimum_rate, m)
                r = m - 1

        return minimum_rate