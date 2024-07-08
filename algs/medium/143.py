# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 

        nodelist = []

        cur = head
        dummy = head

        while cur:
            nodelist.append(cur)
            cur = cur.next
        
        lptr = 0
        rptr = len(nodelist) - 1

        while lptr < rptr:
            nodelist[lptr].next = nodelist[rptr]
            lptr += 1

            if lptr == rptr:
                break

            nodelist[rptr].next = nodelist[lptr]
            rptr -= 1

        nodelist[lptr].next = None
        

"""
Throw all of the nodes in an array and then set up L and R pointers,
modifying the next pointers accordingly. 

"""