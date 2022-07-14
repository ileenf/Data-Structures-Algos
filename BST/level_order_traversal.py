# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # N = number of nodes
    # time complexity: O(N) traverse through each node. O(1) to append
    # node values to lists.
    # space complexity: O(N) store N amount of nodes in level
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
    
        level = []
        queue = deque([root])
        
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_level.append(node.val)
            level.append(curr_level)
        return level
