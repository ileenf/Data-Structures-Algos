class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
    
        index_to_chars = defaultdict(set)
        for word in wordList:
            if word != beginWord:
                for i, ch in enumerate(word):
                    index_to_chars[i].add(ch)
        
        queue = deque()
        seen = set()
        queue.append([beginWord, 1])
        
        while queue:
            word, transformations = queue.popleft()
            
            if word == endWord:
                return transformations
            
            for i, ch in enumerate(word):
                for new_ch in index_to_chars[i]:
                    new_word = word[:i] + new_ch + word[i+1:]
                    if new_word in wordList:
                        if new_word not in seen:
                            queue.append([new_word, transformations + 1])
                        seen.add(new_word)
                            
        return 0
        
