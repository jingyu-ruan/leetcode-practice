class LinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
    
    def add_to_left(self, node):
        right = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = right
        right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        
        self.remove(node)
        self.add_to_left(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_left(node)
        else:
            node = LinkedNode(key, value)
            self.cache[key] = node
            self.add_to_left(node)
            
            if len(self.cache) > self.capacity:
                removed = self.tail.prev
                self.remove(removed)
                del self.cache[removed.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)