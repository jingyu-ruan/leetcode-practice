# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(x):
            if not x:
                return 

            dfs(x.left)
            res.append(x.val)
            dfs(x.right)
        
        dfs(root)

        return res