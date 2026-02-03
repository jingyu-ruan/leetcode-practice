from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque([('(', 1, 0)])
        res = []
        while q:
            path, left, right = q.popleft()
            if left == right == n:
                res.append(''.join(path[:]))
            if left <= n:
                if left > right:
                    q.append((path + ')', left, right + 1))
                if left < n:
                    q.append((path + '(', left + 1, right))
        
        return res