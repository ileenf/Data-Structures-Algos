class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None
        def inorder(node, kth):
            
            if node:
                inorder(node.left, kth)
                nonlocal count
                count += 1
                if count == k:
                    nonlocal answer
                    answer = node.val
                
                inorder(node.right, kth)
        inorder(root,k)
        
        return answer
