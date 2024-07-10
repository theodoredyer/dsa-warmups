class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        pass

    def insert(self, node):
        last_mru = self.right.prev
        last_mru.next = node
        node.prev = last_mru
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.capacity < len(self.cache):
            # evict
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



"""
This is a bit of a tricky problem even after identifying the solution due to sheer amount of code that needs to be written here. Essentially in order to 
track this sort of 'least used' principle, while still maintaiing O(1) for overall complexity of basic operations, we need to not track times for each 
individual entity, but instead the relationships between these entities. When we are thinking about relationships, the natural solution is to use linked lists
and specifically in this case doubly linked lists help us arrive at our solution. 

Additionally, to check and see if a node is in the cache we want to set up a dictionary where the key is the provided key, and the value is the actual node
in the doubly linked list so that we can easily access it for removal/addition

"""