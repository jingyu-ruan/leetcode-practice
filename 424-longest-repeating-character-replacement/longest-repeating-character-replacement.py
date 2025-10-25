from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            
            max_freq = max(count.values())

            while i - l + 1 - max_freq > k:
                l += 1
                count[s[l-1]] -= 1
            
            res = max(res, len(s[l:i]) + 1)
        
        return res