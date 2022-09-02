class BrowserHistory:
    def __init__(self, homepage: str):
        self.previous = [homepage] 
        self.next = []

    def visit(self, url: str) -> None:
        self.previous.append(url)
        self.next = []

    def back(self, steps: int) -> str:
        for _ in range(min(steps, len(self.previous)-1)):
            url = self.previous.pop()
            self.next.append(url)
        return self.previous[-1]

    def forward(self, steps: int) -> str:
        for _ in range(min(steps, len(self.next))):
            url = self.next.pop()
            self.previous.append(url)
        return self.previous[-1]
