from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_cnt = len(need)
        l = 0
        res = ''
        res_len = float('inf')
        window = defaultdict(int)
        have = 0

        for r, ch in enumerate(s):
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    have += 1
            
            while have == need_cnt:
                if r - l + 1 < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                
                left_ch = s[l]
                if left_ch in need:
                    window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1

        return res
            

            