class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seenhash = {}
        seenhash[0] = -1
        running_sum = 0

        for idx, element in enumerate(nums):
            running_sum += element
            current_remainder = running_sum % k

            if current_remainder in seenhash:
                prev_idx = seenhash[current_remainder]

                if idx - prev_idx >= 2:
                    return True
            else:
                seenhash[current_remainder] = idx

        return False