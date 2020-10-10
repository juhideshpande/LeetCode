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
        def helper(res, root):
            if not root:
                return
            res.append((str(root.val)))
            helper(res, root.left)
            helper(res, root.right)
        res = []
        helper(res, root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            if not data:
                return None
            cur = data[0]
            root = TreeNode(cur)
            root.left = helper([d for d in data if d < cur])
            root.right = helper([d for d in data if d > cur])
            return root
        if not data:
            return None
        data = data.split(',')
        return helper([int(d) for d in data])
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
