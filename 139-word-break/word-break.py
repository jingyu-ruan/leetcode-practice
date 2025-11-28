class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * n
        for i in range(n):
            if s[:i+1] in word_set:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] and s[j+1:i+1] in word_set:
                    dp[i] = True
        
        return dp[-1]
