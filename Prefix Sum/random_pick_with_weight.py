class Solution:

    def __init__(self, w: List[int]):
        self.boundaries = []

        curr = 0
        for num in w:
            curr += num
            self.boundaries.append(curr)
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.boundaries[-1])

        for i, num in enumerate(self.boundaries):
            if num >= target:
                return i
