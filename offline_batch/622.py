class ListNode:
    def __init__(self, val, next, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value):
        if self.isFull():
            return False
        
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur

        self.space -= 1
        return True

    def deQueue(self):
        # this might be wrong
        if self.isEmpty():
            return False
        
        tmp = self.left.next
        self.left.next = tmp.next
        tmp.next.prev = self.left

        self.space += 1

        return True

    def Front(self):
        if not self.isEmpty():
            return self.left.next.val
        return -1

    def Rear(self):
        if not self.isEmpty():
            return self.right.prev.val
        return -1

    def isEmpty(self):
        return self.left.next == self.right

    def isFull(self):
        return self.space == 0