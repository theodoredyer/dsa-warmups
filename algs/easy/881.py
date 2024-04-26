class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        minboats = 0

        first = 0
        last = len(people)-1

        while first <= last:
            if first == last:
                return (minboats + 1)
            if people[last] + people[first] > limit:
                minboats += 1
                last -= 1
            else:
                minboats += 1
                last -= 1
                first += 1

        return minboats