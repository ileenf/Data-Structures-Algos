# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # N = number of nodes
    # time complexity: O(N), visit each node
    # space complexity: O(N), store each node in dict
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = defaultdict(list)
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            curr_height = max(left_height, right_height)+1
            nonlocal leaves
            leaves[curr_height].append(node.val)
            
            return curr_height 
        dfs(root)
        return leaves.values()
