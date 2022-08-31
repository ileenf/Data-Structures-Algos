class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_map = dict()
    
    def search_for_timestamp(self, values, timestamp):
        start = 0
        end = len(values)-1
        
        while start <= end:
            mid = (start + end)//2
            
            if values[mid][0] <= timestamp:
                start = mid + 1
            else:
                end = mid - 1
        if values[end][0] <= timestamp:
            return values[end][1]
        return ''

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [[timestamp, value]]
        else:
            self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ''
        values = self.time_map[key]
        return self.search_for_timestamp(values, timestamp)
        
