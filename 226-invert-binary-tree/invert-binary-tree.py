# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            left = node.left if node.left else None
            right = node.right if node.right else None
            node.right = left
            node.left = right

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root
                