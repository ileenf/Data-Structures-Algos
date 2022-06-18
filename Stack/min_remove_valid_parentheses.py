class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idxs_to_keep = set()
        valid = ''
        stack = []
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append([ch, i])
            elif ch == ')':
                if stack:
                    ele, idx = stack.pop()
                    if ele == '(':
                        idxs_to_keep.add(i)
                        idxs_to_keep.add(idx)
            else:
                idxs_to_keep.add(i)
        
     
        for i, ch in enumerate(s):
            # constant time to check in sets
            if i in idxs_to_keep:
                valid += ch
        
        return valid
        
