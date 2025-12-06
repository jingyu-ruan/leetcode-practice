class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        last_end = 0
        idx = {}
        for i, v in enumerate(s):
            if v not in idx:
                idx[v] = i
                res = max(res, i - last_end + 1)
            else:
                last_end = idx[v] + 1
                for val in list(idx.keys()):
                    if idx[val] < last_end:
                        del idx[val]
                idx[v] = i
        
        return res