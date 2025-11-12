# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(node, targetSum):
            if not node:
                return
            if node.val == targetSum:
                self.res += 1

            dfs(node.left, targetSum - node.val)
            dfs(node.right, targetSum - node.val)
        
        def pos(node):
            if not node:
                return 
            dfs(node, targetSum)
            pos(node.left)
            pos(node.right)

        pos(root)
        return self.res