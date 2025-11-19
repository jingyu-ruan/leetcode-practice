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
        if not head:
            return None
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            new_node = dic[cur]
            new_node.next = dic.get(cur.next)
            new_node.random = dic.get(cur.random)
            cur = cur.next

        return dic[head]