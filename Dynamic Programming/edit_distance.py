class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                insert = dp[i][j-1] + 1
                delete = dp[i-1][j] + 1
                replace = dp[i-1][j-1] + (word1[i-1] != word2[j-1])
                dp[i][j] = min(insert, delete, replace)
            
        return dp[n][m]