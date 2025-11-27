# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        pre_i = n - 1
        def dfs(l, r):
            if l > r:
                return
            nonlocal pre_i
            nodeval = postorder[pre_i]
            node = TreeNode(nodeval)
            m = inorder.index(nodeval)
            pre_i -= 1
            node.right = dfs(m + 1, r)
            node.left = dfs(l, m - 1)
            

            return node
        
        return dfs(0, n - 1)