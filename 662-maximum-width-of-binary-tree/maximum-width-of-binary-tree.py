# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        0
        -1 1
        -2 2
        -3 1
        '''
        q = deque([(root, 0)])
        res = 1
        while q:
            n = len(q)
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(n):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))
            
        
        return res