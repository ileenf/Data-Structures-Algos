class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()
        def min_cost(idx):
            if idx >= len(cost):
                return 0
            
            if idx in memo:
                return memo[idx]
            cost_for_one_step = cost[idx] + min_cost(idx+1)
            cost_for_two_step = cost[idx] + min_cost(idx+2)
            
            memo[idx] = min(cost_for_one_step, cost_for_two_step)
            return memo[idx]
        
        return min(min_cost(0), min_cost(1))
