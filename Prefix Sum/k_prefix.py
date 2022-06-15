class Solution:
    # prefix sum
    def solve(self, nums, k):
        prefixes = [0]

        total = 0
        for num in nums:
            total += num
            prefixes.append(total)
            
            
        for i in range(len(prefixes)-1, 0, -1):
            if prefixes[i] <= k:
                return i - 1
        return -1

    # two passes
    def solve(self, nums, k):
        total = sum(nums)
        for i in range(len(nums)-1, -1, -1):
            if total <= k:
                return i
            total -= nums[i]
        return -1
