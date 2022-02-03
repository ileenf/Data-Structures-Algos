class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_house(nums):
            n = len(nums)
            dp = [0 for _ in range(n+1)]
            dp[n] = 0
            dp[n-1] = nums[n-1]

            for i in range(n-2, -1, -1):
                dp[i] = max(nums[i] + dp[i+2], dp[i+1])
                
            return dp[0]
        
        if len(nums) == 1:
            return nums[0]
        return max(rob_house(nums[1:]), rob_house(nums[:-1]))
