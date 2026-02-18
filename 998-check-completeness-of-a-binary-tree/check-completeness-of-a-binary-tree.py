# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        is_last_level = False
        while q:
            node = q.popleft()
            if node.left:
                if not is_last_level:
                    q.append(node.left)
                else:
                    return False
            else:
                is_last_level = True

            if node.right:
                if not is_last_level:
                    q.append(node.right)
                else:
                    return False
            else:
                is_last_level = True

        return True
            