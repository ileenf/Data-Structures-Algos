class Solution:
    # recursion with memoization 
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n+1)]
        
        def climb(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if memo[n] > 0:
                return memo[n]
              
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        
        return climb(n)
   
    # dp
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
