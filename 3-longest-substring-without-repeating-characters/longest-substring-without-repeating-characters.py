class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
           l
        -1 0 1 2 3
        #  a b c a
        t m m z u x t
        0 1 2 3 4 5 6 
        '''
        hist = dict()
        l = 0
        res = 0
        for i, ch in enumerate(s):
            if ch not in hist:
                hist[ch] = i
                res = max(res, i - l + 1)
            else:
                l = max(hist[ch] + 1, l)
                hist[ch] = i
                res = max(res, i - l + 1)
        
        return res
