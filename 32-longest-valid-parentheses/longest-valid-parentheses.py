class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        stk = [-1]
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            if ch == ')':
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    max_len = max(max_len, i - stk[-1])
        
        return max_len