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
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            max_profit = max(max_profit, prices[i] - buy_price)

        return max_profit
