# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)
        res = float('inf')
        n = len(vals)
        for i in range(1, n):
            res = min(res, vals[i] - vals[i-1])

        return res
        