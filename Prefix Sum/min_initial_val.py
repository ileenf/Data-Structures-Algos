class Solution:
    def solve(self, nums):
        if not nums:
            return 1

        prefixes = [0]

        total = 0
        for num in nums:
            total += num
            prefixes.append(total)

        return abs(min(prefixes)) + 1
