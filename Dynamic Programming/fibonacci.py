class Solution:
    # dp
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    
    # recursion with memoization
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        
        def recur(n):
            if n in memo:
                return memo[n]

            memo[n] = recur(n-1) + recur(n-2)
            return memo[n]
            
        return recur(n)
