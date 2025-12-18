class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        l, r = 1, x // 2
        while l <= r:
            m = (l + r) // 2
            if m * m < x:
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m
        
        return r
        