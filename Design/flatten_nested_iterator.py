# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


## flatten nested list into a 1d array
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened_list = []
        def flatten_list(nested_list):
            for item in nested_list:
                if item.isInteger():
                    self.flattened_list.append(item.getInteger())
                else:
                    flatten_list(item.getList())
        flatten_list(nestedList)
        self.pos = 0
    
    def next(self) -> int:
        val = self.flattened_list[self.pos]
        self.pos += 1
        return val
    
    def hasNext(self) -> bool:
        return self.pos < len(self.flattened_list)


## using a stack to solve in an iterative way
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:        
        while self.stack:
            item = self.stack.pop()

            if item.isInteger():
                return item
            
            for nested in reversed(item.getList()):
                self.stack.append(nested)

    def hasNext(self) -> bool:
        while self.stack:
            item = self.stack[-1]

            if item.isInteger():
                return True
            
            self.stack.pop()
            for nested in reversed(item.getList()):
                self.stack.append(nested)
        return False


## more elegant stack solution
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))
    
    def make_stack_top_an_integer(self):
        while self.stack and not self.stack[-1].isInteger():
            item = self.stack.pop()
            
            for nested in reversed(item.getList()):
                self.stack.append(nested)

    def next(self) -> int:        
        self.make_stack_top_an_integer()
        return self.stack.pop()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0
