class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(path, left, right):
            if left == right == 0:
                res.append(path)
                return
            
            if left > 0:
                dfs(path + '(', left - 1, right)
            
            if right > 0 and left < right:
                dfs(path + ')', left, right - 1)
        
        dfs('', n, n)
        return res