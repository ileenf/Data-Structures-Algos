class Leaderboard:
    def __init__(self):
        self.leaderboard = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.leaderboard[playerId] += score
        
    def top(self, K: int) -> int:
        sorted_leaderboard = sorted(self.leaderboard.values(), reverse = True)
        return sum(sorted_leaderboard[:K])

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0
