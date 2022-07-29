class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches_pattern(word, pattern):
            mapping1 = dict()
            mapping2 = dict()
            
            for i in range(len(word)):
                if word[i] not in mapping1:
                    mapping1[word[i]] = pattern[i]
                else:
                    if mapping1[word[i]] != pattern[i]:
                        return False
                if pattern[i] not in mapping2:
                    mapping2[pattern[i]] = word[i]
                else:
                    if mapping2[pattern[i]] != word[i]:
                        return False
            return True
                
        answer = []
        
        for word in words:
            if matches_pattern(word, pattern):
                answer.append(word)
        return answer
