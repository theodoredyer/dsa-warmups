class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)

        ret_arr = []

        for num in snums:
            if len(ret_arr) == 0:
                ret_arr.append([num])
            else:
                need_append = True
                for arr in ret_arr:
                    if num not in arr and need_append is True:
                        arr.append(num)
                        need_append = False
                if(need_append):
                    ret_arr.append([num])
        
        return ret_arr