# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
"""
Sort of as simple as it seems, just remember to do the last check when we only have one list
remaining to grab the rest of it

Traverse item by item in list1/list2 while either of them have remaining elements, set node.next
to the lower of these two list heads and then set node to node.next after and run it back. 

"""