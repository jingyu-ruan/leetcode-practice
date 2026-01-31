class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        word = dict()
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in word:
                word[s[i]] = i
            else:
                l = max(word[s[i]] + 1, l)
                word[s[i]] = i
            res = max(res, i - l + 1)
        return res
