# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        pre_i = 0
        def dfs(l, r):
            nonlocal pre_i
            if l > r:
                return None

            root = TreeNode(preorder[pre_i])
            mid = inorder.index(preorder[pre_i])
            pre_i += 1

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, n - 1)