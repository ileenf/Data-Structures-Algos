class Solution:
    def rangeUpdate(self, nums, operations):
        n = len(nums)
        increases = [0 for _ in range(n+1)]
        for L, R, X in operations:
            increases[L] += X
            increases[R+1] -= X

        for i, num in enumerate(nums):
            nums[i] += increases[i]
            increases[i+1] += increases[i]

        return nums
