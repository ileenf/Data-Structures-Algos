class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            k_rows = (left + right) // 2
            coins = k_rows * (k_rows+1) / 2

            if coins == n:
                return k_rows
            elif coins < n:
                left = k_rows + 1
            else:
                right = k_rows - 1
        
        return right
