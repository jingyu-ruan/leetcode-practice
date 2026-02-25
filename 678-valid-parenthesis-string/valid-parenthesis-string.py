class Solution:
    def checkValidString(self, s: str) -> bool:
        max_left = 0
        min_left = 0
        for ch in s:
            if ch == '(':
                max_left += 1
                min_left += 1
            if ch == ')':
                max_left -= 1
                if max_left < 0:
                    return False
                min_left = max(0, min_left - 1)
            if ch == '*':
                max_left += 1
                min_left = max(0, min_left - 1)
        
        return True if max_left >= 0 and min_left <= 0 else False