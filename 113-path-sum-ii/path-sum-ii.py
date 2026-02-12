# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, path):
            nonlocal res
            if not node:
                return
            path2 = path + [node.val]
            if not node.left and not node.right and sum(path2) == targetSum:
                res.append(path2[:])
            dfs(node.left, path2)
            dfs(node.right, path2)
        
        dfs(root, [])
        return res