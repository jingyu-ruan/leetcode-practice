class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = 0
        idx = 0
        n = len(needle)
        res = []
        for i, ch in enumerate(haystack):
            for j in range(len(res)):
                if ch == needle[res[j]]:
                    res[j] += 1
                    if res[j] == n:
                        return i + 1 - n
                else:
                    res[j] = 0
            
            if ch == needle[0]:
                if n == 1:
                    return i
                res.append(1)

        
        return -1