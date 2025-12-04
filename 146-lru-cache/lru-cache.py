class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
    
    def add_to_head(self, node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        nxt.prev = node
    
    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)
    
    def pop(self):
        node = self.tail.prev
        self.remove(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            node.value = value
        else:
            self.cache[key] = Node(key, value)
            node = self.cache[key]
            self.add_to_head(node)

        if len(self.cache) > self.capacity:
            node = self.pop()
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)