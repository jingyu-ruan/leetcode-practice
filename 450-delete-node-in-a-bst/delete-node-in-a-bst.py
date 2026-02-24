# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, key):
            if not node:
                return
            
            if node.val > key:
                node.left = delete(node.left, key)
            elif node.val < key:
                node.right = delete(node.right, key)
            else:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                right = node.right
                cur = right
                while cur.left:        
                    cur = cur.left
                node.val = cur.val
                node.right = delete(node.right, cur.val)
            
            return node
        return delete(root, key)