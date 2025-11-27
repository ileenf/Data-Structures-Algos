# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree_vals = []

        def preorder(node, tree_vals):
            if not node:
                tree_vals.append('None')
                return

            tree_vals.append(str(node.val))
            preorder(node.left, tree_vals)
            preorder(node.right, tree_vals)

        preorder(root, tree_vals)
        return ','.join(tree_vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def build_tree(nodes):
            if nodes[0] == 'None':
                nodes.pop(0)
                return None

            root = TreeNode(nodes[0])
            
            nodes.pop(0)
            root.left = build_tree(nodes)
            root.right = build_tree(nodes)
            return root

        tree_vals = data.split(',')
        return build_tree(tree_vals)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
