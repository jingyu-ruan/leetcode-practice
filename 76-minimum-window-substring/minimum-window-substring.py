from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        cur = defaultdict(int)
        fulfilled = 0
        res_len = float('inf')
        l = 0
        res = ''
        for i, ch in enumerate(s):
            if ch in need:
                cur[ch] += 1
                if cur[ch] == need[ch]:
                    fulfilled += 1
                    while fulfilled == len(need):
                        if (i - l + 1) < res_len:
                            res_len = i - l + 1
                            res = s[l : i+1]
                        letter = s[l]
                        if letter not in need:
                            l += 1
                        else:
                            cur[letter] -= 1
                            l += 1
                            if cur[letter] < need[letter]:
                                fulfilled -= 1
                                                  #   l   i     
        return res