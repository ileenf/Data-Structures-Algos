class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False
 
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(node, -inf, inf)
