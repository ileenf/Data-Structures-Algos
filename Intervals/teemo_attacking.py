class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        intervals = []

        for time in timeSeries:
            if not intervals:
                intervals.append([time, time + duration - 1])
            else:
                start, end = intervals[-1]
                if time > end:
                    intervals.append([time, time + duration - 1])
                else:
                    intervals = intervals[:-1]
                    intervals.append([start, time + duration - 1])
        total = 0
        for start, end in intervals:
            total += (end - start + 1)

        return total
