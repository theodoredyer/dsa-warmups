class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        
        for n, c in seen.items():
            frequency[c].append(n)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if(len(result) == k):
                    return result


        