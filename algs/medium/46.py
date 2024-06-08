class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            head = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(head)
            res.extend(perms)
            nums.append(head)
        return res


"""
Backtracking problem - need to identify the pattern that whenever we are looking
for perms, we want to isolate off the head and then compute all of the permutations
of the remaining numbers, and then add the head back on after computing all of the perms
"""