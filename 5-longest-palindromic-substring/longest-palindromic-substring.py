class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        res = ''
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if (r - l - 1) > max_len:
                max_len = r - l - 1
                res = s[l+1:r]

            l = i
            r = i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l > 1 and (r - l - 1) > max_len:
                max_len = r - l - 1
                res = s[l+1:r]

        return res