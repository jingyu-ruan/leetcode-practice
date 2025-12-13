# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {v: i for i, v in enumerate(inorder)}
        n = len(inorder)
        post_i = n - 1
        def dfs(l, r):
            nonlocal post_i
            if l > r:
                return None
            
            v = postorder[post_i]
            idx = dic[v]
            node = TreeNode(v)
            post_i -= 1
            
            node.right = dfs(idx + 1, r)
            node.left = dfs(l, idx - 1)

            return node

        return dfs(0, n - 1)