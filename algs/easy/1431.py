class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        resarr = []

        for kid in candies:
            if kid + extraCandies >= max_candies:
                resarr.append(True)
                continue
            resarr.append(False)

        return resarr
            

        