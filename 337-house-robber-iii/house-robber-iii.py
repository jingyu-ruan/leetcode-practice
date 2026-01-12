# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                # [不偷该节点, 偷该节点]
                return (0, 0)
            
            # 递归左、右子树（后序遍历：自底向上）
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 1. 如果偷当前节点，那么左右孩子都不能偷
            # 收益 = 当前节点的值 + 左孩子不偷时的收益 + 右孩子不偷时的收益
            rob_current = node.val + left[0] + right[0]
            
            # 2. 如果不偷当前节点，那么左右孩子“可以偷”也可以“不偷”
            # 我们只需要取左孩子两种情况的最大值，加上右孩子两种情况的最大值
            not_rob_current = max(left[0], left[1]) + max(right[0], right[1])
            
            return (not_rob_current, rob_current)

        # 最终结果是根节点“偷”或“不偷”中的最大值
        result = dfs(root)
        return max(result)