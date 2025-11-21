class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        cur = ''
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stk.append((cur, num))
                cur = ''
                num = 0
            elif ch == ']':
                prev_str, k = stk.pop()
                cur = prev_str + cur * k
            else:
                cur += ch

        return cur