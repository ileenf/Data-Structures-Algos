class Solution:
    def minimumTime(self, timeArr: List[int], totalTrips: int) -> int:
        def can_complete(time, timeArr, totalTrips):
            trips = 0
            for t in timeArr:
                trips += (time // t)
            return trips >= totalTrips



        left = 0
        right = max(timeArr) * totalTrips
        
        while left < right:
            mid = (left + right) // 2

            if can_complete(mid, timeArr, totalTrips):
                right = mid
            else:
                left = mid + 1

        return left
