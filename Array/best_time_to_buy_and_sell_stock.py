class Solution:
    # N = length of array
    # time complexity: O(N), iterate through array once
    # space complexity: O(1), only storing integers in variables
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices) + 1
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
            
