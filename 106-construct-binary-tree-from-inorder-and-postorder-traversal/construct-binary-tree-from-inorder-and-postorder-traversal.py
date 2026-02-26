# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import 
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        post_i = n - 1
        dic = {v: i for i, v in enumerate(inorder)}
        def dfs(l, r):
            nonlocal post_i
            if l > r:
                return
            val = postorder[post_i]
            m = dic[val]
            post_i -= 1
            node = TreeNode(val)
            node.right = dfs(m + 1, r)
            node.left = dfs(l, m - 1)

            return node
        return dfs(0, n - 1)
