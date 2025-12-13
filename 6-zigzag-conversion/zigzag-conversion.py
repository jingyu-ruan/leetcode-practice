class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        dp = [(['#'] * n) for _ in range(numRows)]
        lr, lc = 0, 0
        i = 0

        while i < n:
            while lr < numRows:
                dp[lr][lc] = s[i]
                i += 1
                if i == n:
                    break
                lr += 1
            lr -= 2
            lc += 1
            if i == n:
                break
            while lr > 0:
                dp[lr][lc] = s[i]
                i += 1
                if i == n:
                    break
                lr -= 1
                lc += 1
        
        res = []
        for row in dp:
            for ch in row:
                if ch != '#':
                    res.append(ch)
        
        return ''.join(res)
                
            

