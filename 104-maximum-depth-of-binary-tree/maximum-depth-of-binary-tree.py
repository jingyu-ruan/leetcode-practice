# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        def find_depth(node):
            if not node:
                return 0
        
            
            return 1 + max(find_depth(node.left), find_depth(node.right))
        
        return find_depth(root)