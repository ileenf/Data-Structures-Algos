# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def recur(node, curr_sum):
            if not node:
                return False
            if not node.left and not node.right:
                return curr_sum - node.val == 0
            return recur(node.left, curr_sum - node.val) or recur(node.right, curr_sum - node.val)
            
        return recur(root, targetSum)
