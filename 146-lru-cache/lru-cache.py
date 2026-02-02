class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
    
    def add_to_head(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add_to_head(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.add_to_head(self.cache[key])
        else:
            node = Node(key, value)
            self.add_to_head(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                node = self.tail.prev
                self.remove(node)
                del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)