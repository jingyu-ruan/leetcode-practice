class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        n = len(intervals)
        if n == 1:
            return res
        for i in range(1, n):
            a, b = intervals[i][0], intervals[i][1]
            if a <= res[-1][1]:
                res[-1][1] = max(b, res[-1][1])
            else:
                res.append([a, b])

        return res
        