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
        q = deque()
        def dfs(node):
            nonlocal q
            if not node:
                return
            q.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        dummy = TreeNode(0)
        cur = dummy
        while q:
            node = q.popleft()
            cur.right = node
            cur = cur.right
            cur.left = None
        cur.left = None
        cur.right = None
        return dummy.right
        