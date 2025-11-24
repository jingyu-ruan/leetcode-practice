class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(str):
            if len(str) == 2 * n:
                res.append(str)
                return
            
            if str.count('(') == str.count(')'):
                dfs(str + '(')
            if str.count('(') > str.count(')'):
                if str.count('(') < n:
                    dfs(str + '(')
                    dfs(str + ')')
                else:
                    dfs(str + ')')
        
        dfs('(')

        return res