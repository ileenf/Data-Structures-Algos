import heapq
class StockPrice:

    def __init__(self):
        self.prices = dict()
        self.latest_timestamp = -1
        self.max_price = []
        self.min_price = []
        heapq.heapify(self.max_price)
        heapq.heapify(self.min_price)


    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heapq.heappush(self.max_price, (-price, timestamp))
        heapq.heappush(self.min_price, (price, timestamp))
        

    def current(self) -> int:
        return self.prices[self.latest_timestamp]
        

    def maximum(self) -> int:
        price, timestamp = heapq.heappop(self.max_price)

        while -price != self.prices[timestamp]:
            price, timestamp = heapq.heappop(self.max_price)
        
        heapq.heappush(self.max_price, (price, timestamp))
        return -price
        

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.min_price)

        while price != self.prices[timestamp]:
            price, timestamp = heapq.heappop(self.min_price)
        
        heapq.heappush(self.min_price, (price, timestamp))
        return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
