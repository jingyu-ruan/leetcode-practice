# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(path, node):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                res += (path * 10 + node.val)
                return
            dfs(path * 10 + node.val, node.left)
            dfs(path * 10 + node.val, node.right)
        
        dfs(0, root)
        return res