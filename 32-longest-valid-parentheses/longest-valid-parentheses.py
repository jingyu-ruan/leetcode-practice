class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            if ch == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        
        return res