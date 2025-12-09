class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2:

            if s[p1] != t[p2]:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
                
        if p1 == n1:
                return True

        return False