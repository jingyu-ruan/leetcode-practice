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

        if len(digits) == 1:
            return letters[digits[0]]

        res = []
        for k in range(len(letters[digits[0]])):
            res.append(letters[digits[0]][k])

        for i in range(1, len(digits)):
            s = digits[i]
            to_append = letters[s]
            for j in range(len(res)):
                for l in to_append:
                    res.append(res[j] + l)

        res = [x for x in res if len(x) == len(digits)]

        return res
