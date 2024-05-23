# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False


# this problem is relatively straightforward, in order to determine if a linked list has a cycle, just keep track of all of the 
# nodes we have already visited inside a set or other data structure, and if we encounter a new node who's next node points to a node
# that we've already seen, then we know there is a cycle. 



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if head.next == None:
            return False

        while fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False



# this is an alternative solution that doesn't use any auxilary memory, utilizing the concept that if there is a cycle, the pointers will never reach None,
# and will eventually intersect at the same node given they are traveling at different speeds. 