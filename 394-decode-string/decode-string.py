class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        word = ''
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch.isalpha():
                word += ch
            if ch == '[':
                stack.append((num, word))
                num = 0
                word = ''
            if ch == ']':
                n, prev = stack.pop()
                word = prev + word * n
        return word