class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # keep track of if valid word ends at dp[i]
        dp = [False for i in range(n + 1)]
        
        # this validates first word
        dp[0] = True
        
        for i in range(1, n + 1):
            for word in wordDict:
                # check that previous word is okay AND that current word is in dictionary
                if dp[i - len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
        return dp[-1]