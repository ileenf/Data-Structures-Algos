class ThroneInheritance:

    def __init__(self, kingName: str):
        self.start = kingName
        self.tree = defaultdict(list)
        self.tree[kingName] = []
        self.is_alive = {kingName: True}
        

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)
        self.is_alive[childName] = True
      

    def death(self, name: str) -> None:
        self.is_alive[name] = False
        

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(name, results):
            if self.is_alive[name] == True:
                results.append(name)
            
            for child in self.tree[name]:
                dfs(child, results)

        dfs(self.start, order)
        return order
