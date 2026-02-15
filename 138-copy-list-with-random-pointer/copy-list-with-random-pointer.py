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
        mirror = {}
        cur = head
        while cur:
            mirror[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            node = mirror[cur]
            node.next = mirror[cur.next] if cur.next else None
            node.random = mirror[cur.random] if cur.random else None
            cur = cur.next
        return mirror[head] if head else None
        