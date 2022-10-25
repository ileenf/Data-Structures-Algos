"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [[interval.start, interval.end] for employee in schedule for interval in employee]
        sorted_sched = sorted(intervals)
        merged = []
        
        for start, end in sorted_sched:
            if not merged:
                merged.append([start, end])
            else:
                prev_end = merged[-1][-1]
                if prev_end >= start:
                    new_end = max(prev_end, end)
                    merged[-1][-1] = new_end
                else:
                    merged.append([start, end])
        
        free = []
        curr_start = None
        for start, end in merged:
            curr_end = start 
            free.append(Interval(curr_start, curr_end))
            curr_start = end
            
        return free[1:]
