# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        node_val = []

        def dfs(node):
            if not node:
                return 
            node_val.append(node.val)
            dfs(node.left) 
            dfs(node.right)
        
        dfs(root)

        node_val.sort()

        return node_val[k - 1]