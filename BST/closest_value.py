# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # inorder traversal
    # n = number of nodes in bst
    # time: O(n), search each node
    # space: O(1)
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        value = inf
        def inorder(node):
            if node:
                inorder(node.left)

                nonlocal value
                if abs(target-node.val) < abs(target-value):
                    value = node.val

                inorder(node.right)
        inorder(root)
        return value
    
    # binary search
    # time: O(log(n)), dividing tree in half each iteration
    # space: O(1)
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        value = inf
        
        def binary_search(node):
                if node:
                    nonlocal value
                    if abs(target-node.val) < abs(target-value):
                        value = node.val
                    
                    if node.val < target:
                        binary_search(node.right)
                    else:
                        binary_search(node.left)

        
        binary_search(root)
        return value
