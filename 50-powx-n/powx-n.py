class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n > 0:
            if n % 2 == 1:      # 当前位是 1
                res *= x
            x *= x              # x = x^2
            n //= 2             # 指数右移一位

        return res

        