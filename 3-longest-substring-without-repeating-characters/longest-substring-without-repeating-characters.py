class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cache = {}
        res = 0
        for i, v in enumerate(s):
            if v in cache:
                l = max(cache[v] + 1, l)
            
            cache[v] = i
            res = max(res, i - l + 1)
        
        return res