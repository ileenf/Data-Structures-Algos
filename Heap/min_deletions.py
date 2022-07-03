import heapq
class Solution:
    # heap
    def minDeletions(self, s: str) -> int:
        freqs = list(Counter(s).values())
        pq = [-f for f in freqs]
        heapq.heapify(pq)
        deletions = 0
        
        while len(pq) > 1:
            top_ele = -heapq.heappop(pq)
            if top_ele == -pq[0] and top_ele != 0:
                top_ele -= 1
                deletions += 1
                heapq.heappush(pq, -top_ele)
                
        return deletions

    # sorting
    def minDeletions(self, s: str) -> int:
        freqs = sorted(Counter(s).items(), key=lambda x: x[1], reverse = True)
        seen = set()
        deletions = 0
        
        for key, val in freqs:
            if val not in seen:
                seen.add(val)
            else:
               while val in seen:
                   deletions += 1
                   val -= 1
               if val != 0:
                   seen.add(val)
                
         return deletions
