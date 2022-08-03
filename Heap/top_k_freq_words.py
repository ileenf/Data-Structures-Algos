class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        counts = Counter(words)
        
        for word, count in counts.items():
            heapq.heappush(res, [-count, word])
        
        k_frequent = []
        for _ in range(k):
            val = heapq.heappop(res)[1]
            k_frequent.append(val)
            
        return k_frequent
