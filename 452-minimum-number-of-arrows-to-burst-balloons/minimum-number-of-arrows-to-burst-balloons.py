class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        res = 0
        l, r = points[0][0], points[0][1]
        n = len(points)

        for i in range(1, n):
            a, b = points[i][0], points[i][1]
            if a > r:
                res += 1
                l, r = a, b
            else:
                l = max(l, a)
                r = min(r, b)
        
        return res + 1