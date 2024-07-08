"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        firstpass_ptr = head
        secondpass_ptr = head
        
        old_to_new = {None: None}

        while firstpass_ptr:
            newnode = Node(firstpass_ptr.val, None, None)
            old_to_new[firstpass_ptr] = newnode
            firstpass_ptr = firstpass_ptr.next

        while secondpass_ptr:
            newnode = old_to_new[secondpass_ptr]
            newnode.next = old_to_new[secondpass_ptr.next]
            newnode.random = old_to_new[secondpass_ptr.random]
            
            secondpass_ptr = secondpass_ptr.next

        return old_to_new[head]
    
"""
Set up a dictionary that populates references from the old (original linked list)
to the corresponding copy (created as a new node in the value of the dict)

Then pass through the dictionary again in order of from a second reference to the original head
and when we're setting the next/random pointers for newnodes, we instead set them based on 
the old_to_new mapping of the old nodes. 

"""