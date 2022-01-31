class Solution:
    def topKFrequent(self, nums: List[int], kth: int) -> List[int]:
        def getTopK(mapping, kth):
            items = list(mapping.items())
            x = random.choice([tup[1] for tup in items])
            
            less_than = dict()
            greater_or_equal = dict()
            
            for k, v in items:
                if v < x:
                    less_than[k] = v
                else:
                    greater_or_equal[k] = v
                    
            if kth == len(greater_or_equal):
                return list(greater_or_equal.keys())
              
            elif kth < len(greater_or_equal):
                return getTopK(greater_or_equal, kth)
              
            else:
                return list(greater_or_equal.keys()) + getTopK(less_than, kth - len(greater_or_equal))
             
        hmap = defaultdict(int)
        
        for num in nums:
            hmap[num] += 1
        
        return getTopK(hmap, kth)
