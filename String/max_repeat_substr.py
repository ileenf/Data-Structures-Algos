class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        concat = word
        repeat_val = 1
        
        while concat in sequence:
            concat += word
            if concat in sequence:
                repeat_val += 1
        return repeat_val
