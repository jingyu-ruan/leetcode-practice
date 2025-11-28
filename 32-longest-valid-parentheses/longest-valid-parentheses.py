class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]      # 栈里放下标，先放个哨兵
        res = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()      # 先尝试匹配一个 '('
                if not stack:
                    # 栈空说明这个 ')' 没法和前面的 '(' 匹配
                    # 把当前下标作为「新的不合法边界」
                    stack.append(i)
                else:
                    # 栈不空，说明有合法匹配
                    # 当前合法长度 = i - 栈顶下标
                    res = max(res, i - stack[-1])

        return res
