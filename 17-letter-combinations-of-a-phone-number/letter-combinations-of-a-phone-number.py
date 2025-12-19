# from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {}
        letters['2'] = ['a', 'b', 'c']
        letters['3'] = ['d', 'e', 'f']
        letters['4'] = ['g', 'h', 'i']
        letters['5'] = ['j', 'k', 'l']
        letters['6'] = ['m', 'n', 'o']
        letters['7'] = ['p', 'q', 'r', 's']
        letters['8'] = ['t', 'u', 'v']
        letters['9'] = ['w', 'x', 'y', 'z']
        res = []
        def dfs(path, i):
            if i == len(digits):
                res.append(path[:])
                return
            
            for j in letters[digits[i]]:
                dfs(path + j, i + 1)

        dfs('', 0)

        return res