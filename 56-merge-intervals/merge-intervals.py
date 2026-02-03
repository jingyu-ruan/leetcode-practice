class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        a, b = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            l, r = intervals[i][0], intervals[i][1]
            if l <= b:
                a = min(a, l)
                b = max(b, r)
            else:
                res.append([a, b])
                a, b = l, r
            if i == len(intervals) - 1:
                res.append([a, b])
                
        return res