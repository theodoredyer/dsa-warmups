# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                # Next batch has less than k elements
                break
            
            start_of_next = kth.next

            cur = groupPrev.next
            prev = kth.next

            while cur != start_of_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur

        

# this problem is conceptually pretty simple, and the difficulty comes from pointer management. Needs very intense attention to detail to not mix up starts of 
# groups and previous groups etc, but the concept is as follows:

# keep track of a node right before the start of a batch you're going to process and call it group_prev'
# - scan ahead to see if the k nodes after this group_prev node exist, if k nodes dont exist then just return the head
# if k more nodes do exist, then we need to do a couple of things
# - first get a reference to the start of the next group
# - perform standard linked list reversal where current pointer should start with group_prev.next, and prev (usually None) is going to be the start of next
# - after performing standard linked list reversal, the next step would be to update the group prev pointer to be at what was previously the start of the last
# group, because this element is now at the end. This item would be the same as group_prev.next because group_prev is still pointing to before the start of this group
# after this, we assign group_prev.next to connect the previously detached linkedlist segment (prev group) to the start of the current group, which is now kth
# then we assign the new group prev to be what was once the start of the group containing kth (aka the old groupprev.next)

# then return dummy.next. 

# Again this problem gets confusing with the pointers but isn't overly complex 