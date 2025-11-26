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
            nonlocal pre_i
            if l > r:
                return None
            
            root_val = postorder[pre_i]
            mid = inorder.index(root_val)
            root = TreeNode(root_val)

            pre_i -= 1

            root.right = dfs(mid + 1, r)
            root.left  = dfs(l, mid - 1)

            return root

        return dfs(0, n - 1)