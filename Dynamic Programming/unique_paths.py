class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]    
                
        return dp[-1][-1]
      
    # improved space complexity
    def uniquePaths(self, m: int, n: int) -> int:
        dp1 = [1 for _ in range(n)]
        dp2 = [1 for _ in range(n)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp2[j] = dp1[j] + dp2[j-1]
                
            dp2, dp1 = dp1, dp2
      
        return dp1[-1]
