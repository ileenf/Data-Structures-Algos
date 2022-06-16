class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixes = []
        max_length = 0
        freqs = {0:-1}
        
        total = 0
        for i, num in enumerate(nums):
            total += (1 if num == 1 else -1)
            
            if total in freqs:
                max_length = max(max_length, i-freqs[total])
            else:
                freqs[total] = i
            
        return max_length
                  
