import random

class Solution:

    def __init__(self, nums: List[int]):
        self.idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.idx_map[num].append(i)
       

    def pick(self, target: int) -> int:
        return random.choice(self.idx_map[target])
