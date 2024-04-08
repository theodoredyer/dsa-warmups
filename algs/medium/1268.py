class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        l, r = 0, len(products) - 1

        for i in range(len(searchWord)):
            curchar = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != curchar):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != curchar):
                r -= 1

            res.append([])
            words_in_range = r - l + 1

            for k in range(min(3, words_in_range)):
                res[-1].append(products[l + k])

        return res