class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        potentially_valid_triplets = []

        for triplet in triplets:
            valid_triplet = True
            for i in range(3):
                if triplet[i] > target[i]:
                    valid_triplet = False
            if valid_triplet:
                potentially_valid_triplets.append(triplet)

        for i in range(3):
            tarval = target[i]
            found = False
            for triplet in potentially_valid_triplets:
                if triplet[i] == tarval:
                    found = True
            if found == False:
                return False
        return True


"""
Given that our only operation we can use for altering our temp triplet is max,
we need to make sure that first of all, if we are ever maxing a triplet that has any 
values that are greater than our target values - this will brick our current iteration. 

SO we need to check and see which subset of triplets are actually able to be used, and then 
just search within that subset of triplets index by index to see if we have a triplet that has the target
value at each index, if so we can just take the max of everything and arrive at the target
considering we've already removed the ones that are above max. 

"""