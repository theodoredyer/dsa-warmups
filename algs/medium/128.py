class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0

        for num in numset:
            if num-1 not in numset:
                current_streak = 1
                streak_running = True
                while streak_running:
                    if num + current_streak in numset:
                        current_streak += 1
                    else:
                        streak_running = False

                    longest = max(current_streak, longest)
        return longest
