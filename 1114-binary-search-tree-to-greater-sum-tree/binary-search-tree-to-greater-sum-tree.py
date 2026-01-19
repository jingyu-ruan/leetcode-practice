# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        inorder = []
        def ino(node):
            if not node:
                return
            ino(node.right)
            inorder.append(node.val)
            node.val = sum(inorder[:])
            ino(node.left)
        ino(root)
        return root