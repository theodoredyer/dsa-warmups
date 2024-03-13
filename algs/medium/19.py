# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        lptr = dummy
        rptr = head

        for i in range(n):
            rptr = rptr.next

        while rptr:
            lptr = lptr.next
            rptr = rptr.next

        node_to_remove = lptr.next
        lptr.next = node_to_remove.next

        return dummy.next