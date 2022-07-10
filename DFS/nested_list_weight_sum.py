# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    # N = number of nested elements
    # time complexity - O(N) since we traverse through each nested component
    # space complexity - O(N) since there will be at most N recursive stacks (worst case 
    # if entire list was just nesting) and at most N nested elements in queue
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # dfs is more intuitive here
        def dfs(val, depth):
            total = 0
            for nested in val:
                if nested.isInteger():
                    total += (nested.getInteger() * depth)
                else:
                    total += dfs(nested.getList(), depth+1)

            return total
        return dfs(nestedList, 1)
        
        # alternative bfs solution
        def bfs():
            stack = [[nestedList, 1]]
            total = 0
            
            while stack:
                val, depth = stack.pop()
                for nested in val:
                    if nested.isInteger():
                        total += (nested.getInteger() * depth)
                    else:
                        stack.append([nested.getList(), depth+1])
            return total
        return bfs()
