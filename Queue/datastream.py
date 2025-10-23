class DataStream:
    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.value = value
        self.k = k
        self.count = 0
        

    def consec(self, num: int) -> bool:
        if len(self.stream) >= self.k:
            val = self.stream.popleft()
            if val == self.value:
                self.count -= 1

        if num == self.value:
            self.count += 1
        self.stream.append(num)

        return self.count == self.k
        
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
