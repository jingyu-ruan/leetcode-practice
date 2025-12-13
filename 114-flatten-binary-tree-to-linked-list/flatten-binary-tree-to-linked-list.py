# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            preorder = []

            def dfs(node):
                if not node:
                    return
                
                preorder.append(node)
                dfs(node.left)
                dfs(node.right)
            
            dfs(root)
            
            # cur = root
            for i in range(len(preorder) - 1):
                preorder[i].left = None
                preorder[i].right = preorder[i + 1]
            
            preorder[-1].left = None
            preorder[-1].right = None

            
                