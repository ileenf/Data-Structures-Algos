class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict
        self.words_to_idxs = self.get_words_to_idxs()
    
    def get_words_to_idxs(self):
        words_to_idxs = defaultdict(list)
        
        for idx, word in enumerate(self.words):
            words_to_idxs[word].append(idx)
        return words_to_idxs
        
    def shortest(self, word1: str, word2: str) -> int:
        word1_idxs = self.words_to_idxs[word1]
        word2_idxs = self.words_to_idxs[word2]
        
        shortest_dist = len(self.words)
        
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(word1_idxs) and idx2 < len(word2_idxs):
                shortest_dist = min(shortest_dist, abs(word1_idxs[idx1]-word2_idxs[idx2]))
                if word1_idxs[idx1] < word2_idxs[idx2]:
                    idx1 += 1
                else:
                    idx2 += 1
                     
        return shortest_dist
