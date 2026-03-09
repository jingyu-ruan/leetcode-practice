class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        sign = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in ('+', '-', '*', '/') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(stack.pop() / num))
                
                num = 0
                sign = ch
        
        return sum(stack)