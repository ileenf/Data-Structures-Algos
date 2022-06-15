class Solution:
    # prefix sum 
    def solve(self, nums):
        n = len(nums)
        left_sums = []
        right_sums = []

        left_sum = 0
        right_sum = 0
        for i in range(n):
            left_sums.append(left_sum) 
            right_sums.append(right_sum)

            left_sum += nums[i]  
            right_sum += nums[n-i-1]   
            
        right_sums = right_sums[::-1]
        
        for i in range(len(left_sums)):
            if left_sums[i] == right_sums[i]:
                return i
        return -1

    # two passes
    def solve(self, nums):
        r = sum(nums)
        l = 0

        for i, num in enumerate(nums):
            r -= num
            if l == r:
                return i
            l += num
            
        return -1
