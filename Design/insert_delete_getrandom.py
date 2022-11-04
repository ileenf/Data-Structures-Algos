import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.val_to_idx = dict()
        self.vals = list()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.val_to_idx:
            self.val_to_idx[val] = len(self.vals)
            self.vals.append(val)
            return True
        return False
            
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val in self.val_to_idx:
            last_ele = self.vals[-1]
            remove_idx = self.val_to_idx[val]
            
            self.vals[remove_idx] = last_ele
            self.val_to_idx[last_ele] = remove_idx
            self.vals.pop()
            del self.val_to_idx[val]
            return True
          
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
