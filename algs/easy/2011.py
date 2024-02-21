class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        fin_val = 0
        for item in operations:
            if "--" in item:
                fin_val -= 1
            if "++" in item:
                fin_val += 1
        return fin_val

        