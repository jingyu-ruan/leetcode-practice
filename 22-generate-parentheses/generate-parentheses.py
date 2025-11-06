class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ["()"]

        res = []

        def bt(path, left, right):
            if left == 0 and right == 0:
                res.append(path)
                return
            
            if left > 0:
                bt(path + '(', left - 1, right)
            if right > left:
                bt(path + ')', left, right - 1)

        bt('', n, n)

        return res


            