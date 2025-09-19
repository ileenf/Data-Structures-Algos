class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.token_expiration = dict()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_expiration[tokenId] = currentTime + self.ttl
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.token_expiration:
            return 
        if currentTime >= self.token_expiration[tokenId]:
            return

        self.token_expiration[tokenId] = currentTime + self.ttl
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, expiration in self.token_expiration.items():
            if expiration > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
