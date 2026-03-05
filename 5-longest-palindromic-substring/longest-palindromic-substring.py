class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0
        n = len(s)
        for i, ch in enumerate(s):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > res_len:
                res_len = r - l - 1
                res = s[l+1:r]
            
            l, r = i - 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > res_len:
                res_len = r - l - 1
                res = s[l+1:r] 
        
        return res