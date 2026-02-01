class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ''
        length = 0
        for i in range(len(s) - 1):
            l, r = i, i
            while l >= 1 and r < len(s) - 1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            if r - l + 1 > length:
                length = r - l + 1
                res = s[l:r+1]
        
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > length:
                length = r - l - 1
                res = s[l+1:r]
        
        return res