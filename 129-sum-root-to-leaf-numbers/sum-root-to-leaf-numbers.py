# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, nums):
            if not node:
                return
            if not node.left and not node.right:
                nonlocal res
                res += nums * 10 + node.val

            dfs(node.left, nums * 10 + node.val)
            dfs(node.right, nums * 10 + node.val)

        dfs(root, 0)
        return res