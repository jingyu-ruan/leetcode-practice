class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, path):
            if left == right == n:
                res.append(''.join(path[:]))
                return
                
            if left == n or left > right:
                dfs(left, right + 1, path + [')'])
            if left < n:
                dfs(left + 1, right, path + ['('])
        
        dfs(0, 0, [])
        return res
                
