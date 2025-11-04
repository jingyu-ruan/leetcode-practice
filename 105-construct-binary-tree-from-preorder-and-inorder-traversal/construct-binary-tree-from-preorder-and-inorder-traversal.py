# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        inorder_root_index = inorder.index(root_val)

        inorder_left_team = inorder[0 : inorder_root_index]
        inorder_right_team = inorder[inorder_root_index + 1 : ]

        left_team_size = len(inorder_left_team)
        
        preorder_left_team = preorder[1 : 1 + left_team_size]
        preorder_right_team = preorder[1 + left_team_size : ]

        root.left = self.buildTree(preorder_left_team, inorder_left_team)
        root.right = self.buildTree(preorder_right_team, inorder_right_team)

        return root

