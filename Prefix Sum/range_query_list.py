class RangeSum:
    def __init__(self, nums):
        self.nums = nums
        self.prefixes = self.get_prefixes(self.nums)
        
    def get_prefixes(self, nums):
        prefixes = [0]
        total = 0

        for num in nums:
            total += num
            prefixes.append(total)
        return prefixes

    def total(self, i, j):
        return self.prefixes[j] - self.prefixes[i]
