class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for element in nums:
            if element in seen:
                return True
            else:
                seen[element] = True

        return False