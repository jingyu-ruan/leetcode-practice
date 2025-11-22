class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key = lambda x: x[0])

        res = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            a, b = intervals[i][0], intervals[i][1]
            # c, d = intervals[i+1][0], intervals[i+1][1]
            if r >= a:
                l = min(l, a)
                r = max(b, r)
            else:
                res.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
            if i == len(intervals) - 1:
                res.append([l, r])

        return res