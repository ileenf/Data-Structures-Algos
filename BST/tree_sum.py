# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        root.val = root.val + self.helper(root.left) + self.helper(root.right)
        return root.val
    

    def solve(self, root):
        self.helper(root)
        return root
