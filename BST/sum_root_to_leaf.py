# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import reduce
class Solution:
    # string conversion to int
    def sumNumbers(self, root: TreeNode) -> int:
        numbers = []
        def path(node, num):
            if not node:
                return
            if not node.left and not node.right:
                nonlocal numbers
                numbers.append(num + str(node.val))
                return
            
            path(node.left, num + str(node.val))
            path(node.right, num + str(node.val))
        
        path(root, '')
        if len(numbers) == 1:
            return int(numbers[0])
        return reduce(lambda a, b: int(a)+int(b), numbers)
      
      # no conversion (faster)
      def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        def path(node, num):
            if not node:
                return
            
            curr_val = (num * 10 + node.val)
            if not node.left and not node.right:
                nonlocal total
                total += curr_val
                return
            
            path(node.left, curr_val)
            path(node.right, curr_val)
        
        path(root, 0)
        return total
