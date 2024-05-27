class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow_2 = 0

        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow



"""
This problem is a bit ridiculous under the constraints of O(1) memory and without modifying the existing array, and it forces us to use Floyd's algorithm. 
this essentially states that we just set up fast and slow pointers and traverse the array as if it represented a linked list, because it is vals 0->n

and then when our values collide we know that a cycle occurs (result of duplicate values somewhere else) and to identify that cycle we traverse again, 
by creating a new slow pointer and iterating slow2 and slow until they intersect, then we have our value. 

Alternatively if we are allowed to modify the input array, we can use the negative marking trick to identify if we have already visited a site before:
iterate through the array, and mark the value at the index as negative, when we encounter a negative number already, 
we know that we already saw it once before and should mark it as the duplicate. 
"""