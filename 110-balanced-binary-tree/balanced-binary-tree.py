# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def deep(node):
            if not node:
                return 0
            return 1 + max(deep(node.left), deep(node.right))

        def dfs(node):
            if not node:
                return True
            left = deep(node.left) if node.left else 0
            right = deep(node.right) if node.right else 0
            if abs(left - right) > 1:
                return False
            a = b = True
            if node.left:
                a = dfs(node.left)
            if node.right:
                b = dfs(node.right)
            return a and b
        
        return dfs(root)