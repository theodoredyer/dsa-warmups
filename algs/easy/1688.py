class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        remaining_teams = n

        while remaining_teams > 1:

            if(remaining_teams == 2):
                matches += 1
                break

            matches += int(remaining_teams/2)

            if(remaining_teams % 2 == 0):
                remaining_teams /= 2
            else:
                remaining_teams = int(remaining_teams/2) + 1

        return matches
