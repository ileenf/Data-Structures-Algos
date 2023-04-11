import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def all_bananas_consumed(k, piles):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            if all_bananas_consumed(k, piles):
                right = k
            else:
                left = k + 1
        return left
