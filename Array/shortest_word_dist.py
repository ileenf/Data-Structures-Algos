class Solution:
    # N = length of wordsDict
    # M = length of word1 + length of word2
    # time complexity: O(N*M), iterate once through wordsDict and updating variables
    # takes constant time. each iteration compares the current word against word1 or word2
    # space complexity: O(1), only storing variables that hold integers
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        start = None
        end = None
        min_dist = len(wordsDict)
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                start = i
            elif word == word2:
                end = i
            
            if start != None and end != None:
                min_dist = min(min_dist, abs(start-end))
        return min_dist
