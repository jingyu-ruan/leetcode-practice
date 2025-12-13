# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_i = 0
        def dfs(l, r):
            nonlocal pre_i
            if l > r:
                return None

            v = preorder[pre_i]
            idx = inorder.index(v)
            node = TreeNode(v)
            pre_i += 1

            node.left = dfs(l, idx - 1)
            node.right = dfs(idx + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)

        
            
