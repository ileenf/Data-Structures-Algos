class Solution:
    # sliding window
    # S = len(s)
    # T = len(t)
    # time complexity: O(S^2), interate through s in nested while loop
    # space complexity: O(S+T), store occurences of each letter in s and t.
    # worst case when all letters are unique. 
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        length_s = len(s)
        length_t = len(t)
        if length_s < length_t:
            return ''
        
        t_occur = Counter(t)
        
        def is_desired(window_occur, string_occur):    
            for k, v in string_occur.items():
                occur = window_occur[k]
                if occur < v:
                    return False
            return True
        
        i = 0
        j = 0
        min_length = length_s + 1
        min_substring = ''
        window_counts = defaultdict(int)
        
        while i < length_s:
            while j < length_s:
                window_counts[s[j]] += 1
                if is_desired(window_counts, t_occur):
                    if (j-i) < min_length:
                        min_length = j-i
                        min_substring = s[i:j+1]
                    break
                else:
                    j += 1
            i += 1
            j = i
            window_counts = defaultdict(int)
        return min_substring
                        
