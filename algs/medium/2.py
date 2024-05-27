# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0, None)
        head_reslist = curr

        carry = 0

        while l1 or l2 or carry:
            val_to_add = 0
            if carry:
                val_to_add += 1
                carry = 0
            
            if l2 and not l1:
                val_to_add += l2.val
                l2 = l2.next
            if l1 and not l2:
                val_to_add += l1.val
                l1 = l1.next
            if l1 and l2:
                val_to_add += l1.val + l2.val
                l1, l2 = l1.next, l2.next

            if val_to_add >= 10:
                val_to_add -= 10
                carry = 1
            
            curr.next = ListNode(val_to_add, None)
            curr = curr.next
        return head_reslist.next


"""
This problem is simple conceptually, we are adding two linked lists that represent integers starting from the least significant digit and moving up, if we 
have a value from a list we add it to a pool, accounting for a carryover bit, creating a new node to represent that digit in our result, and then carrying
on from there moving digit by digit. 

important edge cases to note:
- carryovers resulting in carryovers (1 + 9)
- carryovers existing without l1 or l2 existing for the next digit
- list goes on there's so many edge cases. 

"""