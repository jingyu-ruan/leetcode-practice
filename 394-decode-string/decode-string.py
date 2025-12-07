class Solution:
    def decodeString(self, s: str) -> str:
        a = 0
        cur_str = ''
        stack = []
        for ch in s:
            if ch.isdigit():
                a = a * 10 + int(ch)
            elif ch == '[':
                stack.append((a, cur_str))
                a = 0
                cur_str = ''
            elif ch == ']':
                k, strs = stack.pop()
                cur_str = strs + cur_str * k
            else:
                cur_str += ch

        return cur_str


