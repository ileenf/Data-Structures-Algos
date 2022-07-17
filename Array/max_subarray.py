class Solution:
    # N = length of array
    # time complexity: O(N), iterate through array once
    # space complexity: O(1), only storing integers in variables
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf 
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
            
        return max_sum
