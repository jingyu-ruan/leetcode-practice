class Node:
    def __init__(self, val=0, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
    
    def _append_to_head(self, node):
        right = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = right
        right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._append_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._append_to_head(node)
        else:
            node = Node(value, key)
            self.cache[key] = node
            self._append_to_head(node)
            if len(self.cache) > self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)