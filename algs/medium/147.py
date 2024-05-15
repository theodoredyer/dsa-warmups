class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fake_head = ListNode(0, head)

        prev, cur = head, head.next

        while cur:
            if cur.value >= prev.value:

                prev = cur
                cur = cur.next

                continue
            
            scan_node = fake_head
            while scan_node.next.value < cur.value:
                scan_node = scan_node.next

            scan_node_next = scan_node.next
            prev.next = cur.next
            scan_node.next = cur
            cur.next = scan_node_next
            cur = prev.next

        return fake_head.next

            # is this the same thing as:
            # prev.next = cur.next
            # cur.next = tmp.next
            # tmp.next = cur
                    