# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 0

        self.res = 0

        def dfs(node):
            if not node:
                return 0

            lft = dfs(node.left)
            rht = dfs(node.right)

            self.res = max(self.res, lft + rht)

            return 1 + max(lft, rht)

        dfs(root)

        return self.res