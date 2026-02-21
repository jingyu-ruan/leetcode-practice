class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        0 1 2
        0 1 1

        0 2 7
        1 1 
        '''
        n = len(s)
        dp = [0] * (n + 1)
        s = '0' + s
        dp[0] = 1
        if s[1] != '0':
            dp[1] = 1
        else:
            return 0
        for i in range(2, n + 1):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            else: # 1-9
                dp[i] = dp[i-1]
                if (s[i-1] == '1' or s[i-1] == '2') and int(s[i-1] + s[i]) <= 26:
                    dp[i] += dp[i-2]
        
        return dp[-1]
        
