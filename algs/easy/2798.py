class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        met_target = 0
        
        for hour in hours:
            if hour >= target:
                met_target += 1

        return met_target