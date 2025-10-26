class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cur_end = intervals[0][1]
        rm = 0
        for i in range(1, len(intervals)):
            l = intervals[i][0]
            r = intervals[i][1]

            if l < cur_end:
                rm += 1
            else: cur_end = r

        return rm