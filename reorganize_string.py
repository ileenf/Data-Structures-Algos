class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = Counter(s)
        
        max_freq = max(freqs.values())
        
        if (2 * max_freq) - 1 > len(s):
            return ''
        
        chars = [(-v, k) for k, v in freqs.items()]
        heapq.heapify(chars)
        
        
        rearranged = ''
        
        while len(rearranged) < len(s):
            freq, most_common_ch = heapq.heappop(chars)
            freq = abs(freq)
            
            if not rearranged or rearranged[-1] != most_common_ch:
                rearranged += most_common_ch 
                freq -= 1
                
                if freq > 0:
                    heapq.heappush(chars, (-freq, most_common_ch))
            else:
                next_freq, next_most_common_ch = heapq.heappop(chars)
                next_freq = abs(next_freq)
                
                rearranged += next_most_common_ch 
                next_freq -= 1
                if next_freq > 0:
                    heapq.heappush(chars, (-next_freq, next_most_common_ch))
                
                heapq.heappush(chars, (-freq, most_common_ch))
        
        return rearranged
        
