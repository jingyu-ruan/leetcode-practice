class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dic = {}
        res = 0
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = i
                res = max(res, i - l + 1)
            else:
                l = max(l, dic[ch] + 1)
                dic[ch] = i
                res = max(res, i - l + 1)
        
        return res