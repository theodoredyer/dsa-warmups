class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        last_indices = {}

        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_indices:
                last_indices[s[i]] = i

        start_of_partition = 0
        current_pointer = 0
        while start_of_partition < len(s):
            end_of_partition = last_indices[s[start_of_partition]]
            while current_pointer <= end_of_partition:
                end_of_partition = max(end_of_partition, last_indices[s[current_pointer]])
                current_pointer += 1
            res.append(end_of_partition - start_of_partition + 1)
            start_of_partition = end_of_partition + 1
        return res

            
"""
In order to determine the endpoint of a specific interval, we need to create
and auxilary data structure to store (for each character) the last index in which
it occurs, so for example when we're parsing through "a....a" and we are trying to find 
the last index of the char a, if we at any point encounter another character while parsing
that has a last index greater than a, we need to expand the current partition out to 
include the last instance of that other character. 

So we build a map of character / last index and then parse through the string
to apply this logic to sub partitions until we reach the end. 

"""