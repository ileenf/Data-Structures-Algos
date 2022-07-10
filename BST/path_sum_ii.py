# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def recur(node, curr_sum, path):
            if not node:
                return False
            if not node.left and not node.right:
                if curr_sum - node.val == 0:
                    nonlocal paths
                    paths.append(path + [node.val])
            
            return recur(node.left, curr_sum - node.val, path + [node.val]) or recur(node.right, curr_sum - node.val, path + [node.val])
            
        recur(root, targetSum, [])
        return paths
