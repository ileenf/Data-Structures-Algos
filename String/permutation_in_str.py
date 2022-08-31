class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        def check_permutation(s, start, end):
            ch_occur1 = Counter(s)
            ch_occur2 = Counter(s2[start:end+1])
            
            return ch_occur1 == ch_occur2
        start = 0
        end = len(s1)-1
        
        while end < len(s2):
            is_permutation = check_permutation(s1, start, end)
            if is_permutation:
                return True
            start += 1
            end += 1
        return False
