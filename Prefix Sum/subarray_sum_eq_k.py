def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        freqs = defaultdict(int)
        
        total = 0
        for num in nums:
            total += num
            if total == k:
                count += 1
            if total-k in freqs:
                count += freqs[total-k]
                
            freqs[total] += 1
    
        return count 
