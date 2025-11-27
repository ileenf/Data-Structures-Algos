class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_k = 0
        left = 0
        max_consecutive = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                curr_k += 1
            
            while curr_k > k:
                if nums[left] == 0:
                    curr_k -= 1
                left += 1
            
            max_consecutive = max(max_consecutive, right - left + 1)
            
        return max_consecutive
