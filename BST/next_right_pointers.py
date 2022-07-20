"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # N = number of nodes
    # time complexity: O(N), visit every node
    # space complexity: O(N), store each level of tree. last level
    # contains N/2 nodes. O(N/2) = O(N)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
                
        return root
