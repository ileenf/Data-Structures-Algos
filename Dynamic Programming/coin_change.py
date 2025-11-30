class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if amount in memo:
                return memo[amount]
            
            min_amount = math.inf
            for coin in coins:
                total = helper(amount-coin)
                if total != -1:
                    min_amount = min(min_amount, total+1)

            if min_amount != math.inf:
                memo[amount] = min_amount
            else:
                memo[amount] = -1
            return memo[amount]
        
        return helper(amount)
