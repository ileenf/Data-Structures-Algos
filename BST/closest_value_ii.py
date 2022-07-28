# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(node):
                if node:
                    inorder(node.left)
                    heapq.heappush(closest_values, [abs(target-node.val), node.val])
                    
                    inorder(node.right)
                    
        closest_values = []
        heapq.heapify(closest_values)
        inorder(root)
        kth_closest = []
        for _ in range(k):
            val = heapq.heappop(closest_values)
            kth_closest.append(val[1])
            
        return kth_closest
