class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        
        for anagram in strs:
            sorted_anagram = tuple(sorted(anagram))
            hmap[sorted_anagram].append(anagram)
        
        return hmap.values()
