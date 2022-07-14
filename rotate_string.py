class Solution:
    # brute force
    # N = len(s)
    # time complexity: O(N*2), iterating N times and each
    # time doing an operation of O(N), slicing
    # space complexity: O(1), only using pointers to hold variables
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
    
    # time complexity: O(N^2), need to check if substring or not
    # in N+N length s
    # space compexity: O(N), building s+s is 2N length which simplifies     # to O(N)
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s
