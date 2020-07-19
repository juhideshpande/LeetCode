# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
           
            if not stack:
                return True
            node = stack.pop()
            if res and node.val <= res[-1]:
                return False
            res.append(node.val)
            root = node.right
       
