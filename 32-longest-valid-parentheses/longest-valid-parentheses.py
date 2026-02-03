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
                    # 如果栈空了，说明刚才弹出的不是左括号，而是之前的“参照物”
                    # 这意味着当前的 ')' 多余了，它变成了新的“参照物”
                    stack.append(i)
                else:
                    # 如果栈不空，说明匹配成功
                    # 长度 = 当前下标 - 栈顶(即上一个未匹配的位置)
                    res = max(res, i - stack[-1])
        return res
