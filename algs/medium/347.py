class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrances = {}

        for n in nums:
            occurrances[n] = occurrances.get(n, 0) + 1

        frequencies = [[] for i in range(len(nums) + 1)]

        for key, value in occurrances.items():
            frequencies[value].append(key)

        print(frequencies)

        k_added = 0
        ptr = len(frequencies) - 1
        res = []
        while k_added < k:
            for item in frequencies[ptr]:
                res.append(item)
                k_added += 1
                if k_added == k:
                    return res
            ptr -= 1


"""
Set up a dictionary to track the occurrances of each number, and then 
set up a list of lists, where the index of this list represents the frequency
of the number count, and the value of this list is going to be another list containing
all of the characters that have that frequency

We populate this by looking through our dictionary, and for each character we see what the frequency was
and then populate the frequency array at that count to contain that character. 

"""