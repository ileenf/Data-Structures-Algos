# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        max_vals = [root.val]
        queue = [root]

        while queue:
            next_level = []
            vals = []
            for node in queue:
                if not node:
                    continue
                left = node.left
                right = node.right

                if node.left:
                    next_level.append(left)
                    vals.append(node.left.val)
                if node.right:
                    next_level.append(right)
                    vals.append(node.right.val)
                
            if vals:
                max_vals.append(max(vals))

            queue = next_level
        return max_vals


                


        
