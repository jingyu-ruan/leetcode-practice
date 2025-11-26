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
        if root:
            nodes = deque()
            def dfs(node):
                if not node:
                    return
                nodes.append(node)
                dfs(node.left)
                dfs(node.right)
            dfs(root)

            for i in range(1, len(nodes)):
                prev = nodes[i - 1]
                cur = nodes[i]
                prev.left = None
                prev.right = cur