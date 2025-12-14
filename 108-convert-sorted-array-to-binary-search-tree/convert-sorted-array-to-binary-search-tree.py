# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def dfs(l, r):
            if l > r:
                return
            m = (l + r + 1) // 2
            node = TreeNode(nums[m])
            
            node.left = dfs(l, m - 1)
            node.right = dfs(m + 1, r)

            return node
        
        return dfs(0, n - 1)

