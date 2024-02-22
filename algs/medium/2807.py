# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        while current_node and current_node.next:
            next_node = current_node.next
            gcd_val = math.gcd(current_node.val, next_node.val)
            gcd_node = ListNode(val=gcd_val)
            current_node.next = gcd_node
            gcd_node.next = next_node
            current_node = next_node
        
        return head
            
        