from collections import deque
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
        queue = deque(letters[digits[0]])
        n = len(digits)
        if n == 1:
            return letters[digits[0]]
        cur = 1
        while queue and cur < n:
            cur_lst = letters[digits[cur]]
            queue_len = len(queue)
            for _ in range(queue_len):
                word = queue.popleft()
                for l in cur_lst:
                    if cur != n - 1:
                        queue.append(word + l)
                    else:
                        res.append(word + l)
            cur += 1
        
        return res
                

            