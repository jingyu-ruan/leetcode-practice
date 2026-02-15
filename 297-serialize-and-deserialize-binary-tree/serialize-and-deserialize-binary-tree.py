# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """Encodes a tree to a single string."""
        if not root:
            return ''
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                # 只有非空节点才把孩子入队
                q.append(node.left)
                q.append(node.right)
            else:
                # 关键修正：遇到空节点，必须记录 "None"
                res.append("None")
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        vals = data.split(',')
        root = TreeNode(int(vals[0])) # 先建立根节点
        q = deque([root])             # 队列只存"存活"的父节点
        
        i = 1 # 指针，指向 vals 中下一个要处理的值
        
        while q:
            node = q.popleft() # 取出一个父节点
            
            # 1. 尝试找左孩子
            if vals[i] != "None":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left) # 只有非空节点才有资格入队当爹
            i += 1
            
            # 2. 尝试找右孩子
            if vals[i] != "None":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
            
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))