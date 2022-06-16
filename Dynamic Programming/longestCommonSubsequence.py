class Solution:
    # recursion + memoization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = dict()
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                
                memo[(i, j)] =  1 + helper(i-1, j-1)
            else:
                case2 = helper(i-1, j)
                case3 = helper(i, j-1)
                
                memo[(i, j)] = max(case2, case3)
            return memo[(i, j)]
        
        return helper(len(text1)-1, len(text2)-1)
    
    # dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)] 
        
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
              
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[-1][-1]
