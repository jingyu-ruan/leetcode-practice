class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        l, r = 0, x // 2
        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
            else:
                return m
        
        return r

'''
0, 4
m = 2
3, 4
m = 3
3, 2
'''