class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        max_len = 1
        res = s[0]

        for i in range(1, len(s) - 1):
            ch = s[i]
            l = i-1
            r = i+1
            cur_len = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:  # odd
                cur_len += 2
                l -= 1
                r += 1
            if cur_len > max_len:
                max_len = cur_len
                res = s[l+1:r]
        
        for i in range(0, len(s) - 1):
            ch = s[i]
            l = i
            r = i+1
            cur_len = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:  # even
                cur_len += 2
                l -= 1
                r += 1
            if cur_len > max_len:
                max_len = cur_len
                res = s[l+1:r]

        return res
            