# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def compare(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            
            return compare(node.left, lower, node.val) and compare(node.right, node.val, upper)


        return compare(root, float('-inf'), float('inf'))