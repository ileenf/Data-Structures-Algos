class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid_capacity(capacity, weights, days):
            num_days = 0
            curr_cap = 0

            for w in weights:
                curr_cap += w
                
                if curr_cap > capacity:
                    curr_cap = w
                    num_days += 1

            if curr_cap <= capacity:
                num_days += 1
        
            return num_days <= days
                

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if valid_capacity(mid, weights, days):
                right = mid
            else:
                left = mid + 1
        return left
