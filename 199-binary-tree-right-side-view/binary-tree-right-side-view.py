# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if node.left:
                    # res.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    # res.append(node.right.val)
                    queue.append(node.right)
                
                if i == l - 1:
                    res.append(node.val)
                
        return res
