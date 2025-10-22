class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        dic = {')': '(', ']': '[', '}': '{'}
        stk = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stk.append(ch)
            elif ch in dic:
                if not stk:
                    return False 
                    
                if stk[-1] == dic[ch]:
                    stk.pop()
                else:
                    return False
            else:
                return False

        if not stk:
            return True
        else:
            return False