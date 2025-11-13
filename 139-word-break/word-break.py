class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        word_set = set(wordDict)

        for i, ch in enumerate(s):
            if s[:i+1] in word_set:
                dp[i] = True
            for j in range(i):
                if dp[j] and s[j+1:i+1] in word_set:
                    dp[i]   = True

        return dp[-1]