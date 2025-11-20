class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        l = 0
        seen = {}
        res = 0
        for r, ch in enumerate(s):
            if ch in seen and seen[ch] >= l:
                l = seen[ch] + 1
            seen[ch] = r
            res = max(res, r-l+1)

        return res
