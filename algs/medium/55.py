class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endpoint = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= endpoint:
                endpoint = i
        
        return True if endpoint == 0 else False


"""
Can be solved many ways, but simplest is greedy solution. 

Instead of thinking about this by way of incrementing from the start and trying to
find a path, instead we can think about this in terms of shrinking our requirements

starting from the end and moving forwards, if we are at an index where the index 
+ the value at that index is >= the endpoint, then we know if we reach that index we are
able to reach the endpoint. Thus, we can shift our expectations to call this new 
index our endpoint, and we know if we are able to reach that new index on any
future calls that we will be able to reach the true endpoint. 

Thus we track backwards, and update/minimize our endpoint, if we are able to reduce
this value to be i=0 then we know we can reach the true endpoint from the start.

"""