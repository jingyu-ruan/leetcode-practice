class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] != matches[ch]:
                        return False
                    else:
                        stack.pop()
        
        if not stack:
            return True
        else:
            return False
