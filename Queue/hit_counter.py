class HitCounter:
    # store entire history of all hits in hashmap
    def __init__(self):
        self.hits = defaultdict(int)
        

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] += 1
        

    def getHits(self, timestamp: int) -> int:
        total = 0
        
        for time in range(timestamp, timestamp-300, -1):
            total += self.hits[time]
        return total
     
class HitCounter:
    # use a queue to store hits, pop off hits that aren't within 300 secs
    # works because calls to getHits will be chronologically increasing
    def __init__(self):
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append([timestamp, 1])
        

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            front = self.hits[0]
            if timestamp - front[0] >= 300:
                self.hits.popleft()
            else:
                break
        return len(self.hits)
