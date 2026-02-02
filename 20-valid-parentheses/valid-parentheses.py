class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ('{', '(', '['):
                stack.append(ch)
            if ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
            