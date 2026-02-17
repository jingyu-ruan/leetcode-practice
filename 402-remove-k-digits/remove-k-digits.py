class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        n = len(stack)
        l = 0
        while l < n and stack[l] == '0':
            l += 1
        if l == n:
            return '0'
        return ''.join(stack[l:])