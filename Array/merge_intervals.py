class Solution:
    def solve(self, intervals):
        intervals.sort()
        merged = []

        for start, end in intervals:
            if not merged:
                merged.append([start, end])
            else:
                prev_end = merged[-1][1]
                if start <= prev_end:
                    merged[-1][1] = max(end, prev_end)
                else:
                    merged.append([start, end])
        return merged
