class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        retarr = []

        alice_num, bob_num = 0, 0
        nums = sorted(nums)

        while len(nums) > 0:
            alice_num = nums.pop(0)
            bob_num = nums.pop(0)

            retarr.append(bob_num)
            retarr.append(alice_num)

        return retarr



        