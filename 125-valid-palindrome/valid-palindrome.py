class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = []
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                p.append(ch.lower())
        
        if not p:
            return True
        if len(p) == 1:
            return True

        n = len(p)
        m = n // 2
        if n % 2 == 1:
            r = m + 1
            l = m - 1
            while l >= 0 and r <= n - 1:
                if p[l] != p[r]:
                    return False
                r += 1
                l -= 1
            return True
        else:
            r = m
            l = m - 1
            while l >= 0 and r <= n - 1:
                if p[l] != p[r]:
                    return False
                r += 1
                l -= 1
            return True

