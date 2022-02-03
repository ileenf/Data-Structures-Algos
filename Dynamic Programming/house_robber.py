class Solution:
    # recursion + memoization
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        def rob_helper(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            yes_rob = nums[i] + rob_helper(i+2)
            no_rob = rob_helper(i+1)
            memo[i] = max(yes_rob, no_rob)
            return memo[i]
            
        return rob_helper(0)
      
    # iterative
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        dp[n] = 0
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
                
        return dp[0]
     
