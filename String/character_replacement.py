class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        
        start = 0
        max_freq = -1
        longest_repeating = -1
    
        for end in range(len(s)):
            counts[s[end]] += 1
            max_freq = max(max_freq, counts[s[end]])
            
            if (end-start+1) - max_freq <= k:
                longest_repeating = max(longest_repeating, (end-start+1))
            else:
                counts[s[start]] -= 1
                start += 1
        return longest_repeating
