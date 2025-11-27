# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root and (root.left or root.right):
            nodes = deque()
            def preorder(node):
                if not node:
                    return
                nodes.append(node)
                preorder(node.left)
                preorder(node.right)

            preorder(root) 
            cur = root
            for i in range(len(nodes)):
                node = nodes.popleft()
                cur.left = None
                cur.right = node
                cur = cur.right