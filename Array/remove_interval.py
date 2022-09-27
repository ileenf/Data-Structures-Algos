class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remaining = []
        remove_start, remove_end = toBeRemoved
        
        for start, end in intervals:
            
            if end < remove_start or remove_end < start:
                remaining.append([start, end])
            else:

                if start < remove_start:
                    remaining.append([start, remove_start])

                if remove_end < end:
                    remaining.append([remove_end, end])
        
        return remaining
