class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dic = {']': '[', '}': '{', ')': '('}
        for ch in s:
            if ch in ['(', '[', '{']:
                stk.append(ch)
            if ch in [')', ']', '}']:
                if not stk:
                    return False
                elif stk[-1] == dic[ch]:
                    stk.pop()
                else:
                    return False
        
        return True if not stk else False
            