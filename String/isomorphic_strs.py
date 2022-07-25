class Solution:
    # N = lenght of string
    # time complexity: O(N), iterate N times through strings, 
    # other operations during iteration are constant
    # space complexity: O(N), storing two maps of length N
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_s = dict()
        mapping_t = dict()
        for i in range(len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
             
            else:
                if mapping_s[s[i]] != t[i]:
                    return False
                
            if t[i] not in mapping_t:
                mapping_t[t[i]] = s[i]
            else:
                if mapping_t[t[i]] != s[i]:
                    return False
        return True
