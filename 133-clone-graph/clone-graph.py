"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        old_to_new = {}
        old_to_new[node] = Node(node.val)

        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in old_to_new:
                    # 克隆新的邻居
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                
                # 把克隆的邻居加到克隆节点的邻居列表
                old_to_new[cur].neighbors.append(old_to_new[nei])
        
        return old_to_new[node]