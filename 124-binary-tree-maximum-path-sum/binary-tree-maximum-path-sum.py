# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # 以当前节点为拐点的路径和
            price_newpath = node.val + left_gain + right_gain

            # 更新全局最大路径和
            max_sum = max(max_sum, price_newpath)

            # 返回能贡献给父节点的单边最大路径和
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum