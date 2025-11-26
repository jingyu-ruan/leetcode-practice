# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        def dfs(node, need):
            if not node:
                return
            if node.val == need:
                nonlocal res
                res += 1
            
            dfs(node.left, need - node.val)
            dfs(node.right, need - node.val)
        
        def helper(node):
            if not node:
                return
            dfs(node, targetSum)
            helper(node.left)
            helper(node.right)

        helper(root)    
        return res