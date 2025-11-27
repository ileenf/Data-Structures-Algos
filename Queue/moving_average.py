class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.values = []
        self.running_total = 0
        self.count = 0
       

    def next(self, val: int) -> float:
        self.values.append(val)
        self.count += 1

        if self.count > self.size:
            to_remove = self.values.pop(0)
        else:
            to_remove = 0

        self.running_total -= to_remove
        self.running_total += val

        return self.running_total / min(self.count, self.size)
