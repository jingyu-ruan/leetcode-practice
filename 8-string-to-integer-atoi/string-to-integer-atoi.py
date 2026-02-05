class Solution:
    def myAtoi(self, s: str) -> int:
        s2 = s.strip()
        res = 0
        neg = 1
        for i, ch in enumerate(s2):
            if i == 0:
                if ch == '-' or ch == '+':
                    neg = -1 if ch == '-' else 1
                elif ch.isdigit():
                    res = res * 10 + ord(ch) - ord('0')
                else:
                    return 0
            else:
                if ch.isdigit():
                    res = res * 10 + ord(ch) - ord('0')
                else:
                    break            
        
        if neg == 1:
            return min(res, 2 ** 31 - 1)
        else:
            return max(- res, - 2 ** 31)