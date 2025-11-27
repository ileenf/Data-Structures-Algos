class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = [word for word in words[::-1] if word]
        return ' '.join(reversed_words)
