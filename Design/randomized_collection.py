class RandomizedCollection:

    def __init__(self):
        self.collection = [] 
        self.indexes = defaultdict(set)         

    def insert(self, val: int) -> bool:
        self.indexes[val].add(len(self.collection))
        self.collection.append(val)
        return len(self.indexes[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indexes[val]:
            return False
        idx_to_remove = self.indexes[val].pop()
        last_val = self.collection[-1]
    
        self.collection[idx_to_remove] = last_val
        self.indexes[last_val].add(idx_to_remove)
        self.indexes[last_val].remove(len(self.collection)-1)
        
        self.collection.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.collection)
