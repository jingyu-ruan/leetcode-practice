class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        m = newInterval[0]
        n = newInterval[1]
        i = 0

        while i < len(intervals) and m > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= n and intervals[i][1] >= m:
            m = min(m, intervals[i][0])
            n = max(n, intervals[i][1])
            i += 1
        res.append([m, n])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
