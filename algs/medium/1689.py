class Solution:
    def minPartitions(self, n: str) -> int:
        highest_single_int = 0

        strnum = str(n)

        for i in range(len(strnum)):
            current_num = int(strnum[i])
            highest_single_int = max(highest_single_int, current_num)

        return highest_single_int
