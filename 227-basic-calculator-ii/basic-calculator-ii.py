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
            
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    a = stack.pop()
                    stack.append(int(a / num))
                
                num = 0
                sign = ch
        
        return sum(stack)