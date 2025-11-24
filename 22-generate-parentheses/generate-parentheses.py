from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque(['('])
        res = []
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                str = queue.popleft()
                if str.count('(') == str.count(')') and str.count('(') < n:
                    queue.append(str + '(')
                if str.count(')') == n:
                    res.append(str)
                if str.count('(') > str.count(')'):
                    if str.count('(') < n:
                        queue.append(str + '(')
                        queue.append(str + ')')
                    else:
                        queue.append(str + ')')

        return res
                    
