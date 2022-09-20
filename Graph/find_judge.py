class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0 for i in range(n+1)]
        
        for p1, p2 in trust:
            people[p1] += 1
            people[p2] -= 1
        
        for i in range(1, n+1):
            if -people[i] == n-1:
                return i
        return -1
