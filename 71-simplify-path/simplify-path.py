class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ''
        path += '/'
        for ch in path[1:]:
            if ch == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += ch

        res = '' 
        for i in range(len(stack)):
            res = res + '/' + stack[i] 
        
        return res if res else '/'