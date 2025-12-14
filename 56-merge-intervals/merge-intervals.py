class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        res = []
        l, r = intervals[0][0], intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            a, b = intervals[i][0], intervals[i][1]
            if a <= r:
                r = max(r, b)
            else:
                res.append([l, r])
                l, r = a, b
        res.append([l, r])
        return res