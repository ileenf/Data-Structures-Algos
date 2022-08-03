# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.curr_min = root.val
        self.second_min = inf
        
        def search(node):
            if not node:
                return 
            if self.curr_min < node.val < self.second_min:
                self.second_min = node.val

            
            if node.val == self.curr_min:
                search(node.left)
                search(node.right)
        
        search(root)
        
        if self.second_min != inf:
            return self.second_min
        return -1
